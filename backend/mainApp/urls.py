from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("islogin/", views.islogin),
    path("comments/", views.comments),
    path("comments/gen/", views.gen_comments),
    path("js/", views.domcompromise),
    path("sqlgen/", views.create_sample),
    path("sqldemo/", views.getsql),
    path("subscribe/", views.render_mail)
]

"""
Moduł zawierający punkty końcowe (endpoints) dla aplikacji.

Endpoints:
- /register/ : Endpoint do rejestracji użytkownika.
- /login/ : Endpoint do logowania użytkownika.
- /logout/ : Endpoint do wylogowania użytkownika.
- /islogin/ : Endpoint do sprawdzenia stanu zalogowania.
- /comments/ : Endpoint do wyświetlania komentarzy.
- /comments/gen/ : Endpoint do generowania komentarzy.
- /js/ : Endpoint do obsługi kompromitacji DOM (niebezpieczne).
- /sqlgen/ : Endpoint do tworzenia próbek SQL (niebezpieczne).
- /sqldemo/ : Endpoint do pobierania przykładowego SQL (niebezpieczne).
- /subscribe/ : Endpoint do renderowania maila subskrypcyjnego.
"""