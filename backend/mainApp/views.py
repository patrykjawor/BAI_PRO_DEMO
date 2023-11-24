from django.http import JsonResponse, HttpResponse, HttpRequest
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.http import require_http_methods
from django.utils.dateparse import parse_datetime
from .forms import UserForm
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from backend import settings
from traceback import format_exc
from .serializers import CommentSerializer
from .models import Comment, UserProfile
from .decorators import require_login
import sqlite3
import qrcode
from io import BytesIO
from base64 import b64encode

@require_http_methods(['POST'])
def register_view(request):
    """
    Rejestruje nowego użytkownika.

    :param request: HttpRequest object
    :return: JsonResponse z komunikatem o sukcesie/błędzie
    """
    try:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        enable_2fa = request.POST.get('enable_2fa') == 'true'

        form = UserForm({
            'username': username,
            'email': email,
            'password1': password1,
            'password2': password2
        })

        if form.is_valid():
            user = form.save()

            if enable_2fa:
                profile, created = UserProfile.objects.get_or_create(user=user)

                if not profile.totp_device:
                    totp_device = TOTPDevice.objects.create(user=user, confirmed=False)
                    totp_device.save()
                    profile.totp_device = totp_device
                    profile.enable_2fa = enable_2fa
                    profile.save()
        
                    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=0
                    )
                    qr.add_data(totp_device.config_url)
                    qr.make(fit=True)
                    qr_code_img = qr.make_image(fill_color=(66, 184, 131), back_color=(18,18,18))
                    buffer = BytesIO()
                    qr_code_img.save(buffer)
                    buffer.seek(0)
                    encoded_img = b64encode(buffer.read()).decode()
                    qr_code_data = f'data:image/png;base64,{encoded_img}'

                    response_data = {
                    'message': 'User registered successfully',
                    'image_data': qr_code_data
                    }
                else:
                    response_data = {'message': 'User registered successfully (2FA was already enabled)'}
            else:
                response_data = {'message': 'User registered successfully (2FA is disabled)'}
        else:
            return JsonResponse({'error': form.errors}, status=400)

        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    
@require_http_methods(['POST'])
def login_view(request):
    """
    Loguje użytkownika.

    :param request: HttpRequest object
    :return: JsonResponse z komunikatem o sukcesie/błędzie
    """
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            requires_2fa = False

            try:
                user_profile = UserProfile.objects.get(user=user)
                if user_profile.enable_2fa:
                    requires_2fa = True
            except UserProfile.DoesNotExist:
                pass

            if requires_2fa:
                totp_code = request.POST.get('totp_code')
                if totp_code:
                    try:
                        totp_device = TOTPDevice.objects.get(user=user)
                        if totp_device.verify_token(totp_code):
                            login(request, user)
                            return JsonResponse({'message': 'User logged in successfully'})
                        else:
                            return JsonResponse({'error': 'Invalid 2FA code'}, status=400)
                    except TOTPDevice.DoesNotExist:
                        return JsonResponse({'error': '2FA device not found'}, status=400)
                else:
                    return JsonResponse({'requires_2fa': True})
            else:
                login(request, user)
                return JsonResponse({'message': 'User logged in successfully'})
        else:
            return JsonResponse({'error': 'Invalid username or password'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
 
    
@require_http_methods(["POST"])
def logout_view(request):
    """
    Wylogowuje użytkownika.

    :param request: HttpRequest object
    :return: JsonResponse z komunikatem o wylogowaniu
    """
    logout(request)
    return JsonResponse({'message':'User logged out'})


@require_http_methods(['GET'])
@ensure_csrf_cookie
def islogin(request):
    """
    Sprawdza stan zalogowania użytkownika.

    :param request: HttpRequest object
    :return: JsonResponse z informacją o zalogowaniu
    """
    return JsonResponse({"authenticated": request.user.is_authenticated})


@require_http_methods(['GET'])
@require_login
def comments(request:HttpRequest):
    """
    Zwraca listę komentarzy.

    :param request: HttpRequest object
    :return: JsonResponse z listą komentarzy
    """
    return JsonResponse({"comments": CommentSerializer(Comment.objects.all(), many=True).data})


@require_http_methods(['POST'])
@csrf_exempt
@require_login
def gen_comments(request):
    """
    Generuje przykładowe komentarze.

    :param request: HttpRequest object
    :return: JsonResponse z komunikatem o wygenerowanych komentarzach
    """
    if Comment.objects.count() >= 5:
        return JsonResponse({"message": "Already created"})
    Comment(
        title = 'Simple comment',
        comment = 'This is a great example of normal comment',
        date_time = parse_datetime('2023-06-12T18:22:00+02:00')
    ).save()
    Comment(
        title = 'Unharmful comment',
        comment = 'This is a great example of unharmful <strong>comment</strong> with injected HTML &lt;strong&gt; tag.',
        date_time = parse_datetime('2023-08-15T15:32:10+02:00')
    ).save()
    Comment(
        title = 'Somewhat dangerous comment',
        comment = 'This is a great example of dangerous comment <iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ?si=O7ynaNQw9GcNtXud" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe> with injected HTML &lt;iframe&gt; tag.',
        date_time = parse_datetime('2023-09-08T22:40:31+02:00')
    ).save()
    Comment(
        title = 'Pretty dangerous comment',
        comment = 'This is a great example of dangerous comment with <img src onerror="alert(\'injected <script> tag\')"/>',
        date_time = parse_datetime('2023-10-09T00:20:15+02:00')
    ).save()
    Comment(
        title = 'Extremly dangerous comment',
        comment = '<img src onerror="fetch(\'http://localhost:8000/main/js/\').then(response => response.text()).then( text => document.write(text)).catch(error => { })">',
        date_time = parse_datetime('2023-10-12T21:37:00+02:00')
    ).save()
    return JsonResponse({"message": "Comments generated successfully"})


@require_http_methods(["GET"])
# No @require_login -> We simulate hackers website where no login is required.
def domcompromise(request):
    """
    Endpoint do demonstracji kompromitacji DOM.

    :param request: HttpRequest object
    :return: HttpResponse z kodem HTML
    """
    page = get_template("dom.html")
    return HttpResponse(page.render())


@require_http_methods(["POST"])
@require_login
def create_sample(request):
    """
    Tworzy przykładową bazę danych.

    :param request: HttpRequest object
    :return: JsonResponse z komunikatem o sukcesie/błędzie
    """
    try:
        file = open("start.sql", "r")
        conn = sqlite3.connect('sample.sqlite3')
        cursor = conn.cursor()
        cursor.executescript(file.read())
        cursor.close()
        conn.close()
        file.close()
        return JsonResponse({"message": "Sample database created successfully"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@require_http_methods(["GET"])
@require_login
def getsql(request:HttpRequest):
    """
    Zwraca dane z bazy danych.

    :param request: HttpRequest object
    :return: JsonResponse z danymi z bazy
    """
    try:
        conn = sqlite3.connect('sample.sqlite3')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        result = None
        name = request.GET['name'] if 'name' in request.GET else ''
        if 'safe' in request.GET and request.GET['safe'] == 'true':
            result = cursor.execute("""
            SELECT 
                name, 
                price, 
                thumbnail 
            FROM 
                products 
            WHERE 
                name LIKE ?
            """,
                (f'%{name}%',)
            )
        else:
            result = cursor.execute(f"SELECT name, price, thumbnail FROM products WHERE name LIKE '%{name}%'")
        # IMPORTANT #
        # WE ASSUME DEV IS LAZY AND WANTED TO GET EVERY COLUMN FROM QUERY AND RETURN IT TO USER #
        products = [{item: row[item] for item in row.keys()} for row in result]
        cursor.close()
        conn.close()
        return JsonResponse({"products": products, "query": f"SELECT name, price, thumbnail FROM products WHERE name LIKE '%{name}%'"})
    except Exception as e:
        print(e)
        return JsonResponse({"error": str(e), "stack": format_exc()}, status=500)


# @require_http_methods(['POST']) # LAZY DEV DIDN'T ADD REQUIRED METHOD
@require_login # CSRF attack will be successfull - web browser sends cookies by default.
def render_mail(request:HttpRequest):
    """
    Renderuje i wysyła maila subskrypcyjnego.

    :param request: HttpRequest object
    :return: JsonResponse z komunikatem o wysłaniu maila
    """
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Unauthorized. Please log in first!"}, status=401)
    try:
        html = get_template('email.html')
        txt = get_template('email.txt')
        subject, _from, to = 'Important information', settings.EMAIL_HOST_USER, request.user.email
        html_content = html.render({'username': request.user.username})
        text_content = txt.render({'username': request.user.username})
        msg = EmailMultiAlternatives(subject, text_content, _from, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    except Exception as e:
        print(e)
        return JsonResponse({"error": "Unable to send email!"}, status=500)
 
    return JsonResponse({"message": "Email sent successfully!"})