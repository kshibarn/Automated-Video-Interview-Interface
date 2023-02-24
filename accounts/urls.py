from django.urls import path

from . import loginviews
from . import signupviews

urlpatterns = [
    path("register", signupviews.register, name="register"),
    path("login", loginviews.login, name="login"),
    path("logout", loginviews.logout, name="logout")
]