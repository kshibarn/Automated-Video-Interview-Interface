from django.urls import path

from . import views

urlpatterns = [
    path('', views.admin, name='admin'),
    path('setInterview', views.setInterview, name='setInterview'),
    path('checkInterview', views.checkInterview, name='checkInterview')
]