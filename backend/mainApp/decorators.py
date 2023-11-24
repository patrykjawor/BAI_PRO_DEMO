from django.http import HttpRequest, JsonResponse
def require_login(func, *args, **kwargs):
    """
    Sprawdza, czy użytkownik jest zalogowany. Zwraca 401 z komunikatem błędu JSON, jeśli użytkownik nie jest zalogowany.

    """
    def _wrapper(request:HttpRequest):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return JsonResponse({"error": "Please log in first!"}, status=401)
    return _wrapper