from django.urls import path

from AVII.accounts import signupviews

from . import loginviews

urlpatterns = [
    path("register", signupviews.register, name="register"),
    path("login", loginviews.login, name="login"),
    path("logout", loginviews.logout, name="logout")
]