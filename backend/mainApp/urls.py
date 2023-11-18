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