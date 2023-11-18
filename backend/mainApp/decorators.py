from django.http import HttpRequest, JsonResponse

# Checks if user is logged in. Returns 401 with error message if not
def require_login(func, *args, **kwargs):
    """
    Checks whether user is logged in or not. Returns 401 with JSON error message if user is not logged in.

    """
    def _wrapper(request:HttpRequest):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return JsonResponse({"error": "Please log in first!"}, status=401)
    return _wrapper