from django.urls import path

from . import views

app_name = 'adminPanel'

urlpatterns = [
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('setInterview/', views.setInterview, name='setInterview'),
    path('checkInterview/', views.checkInterview, name='checkInterview')
]