from django.urls import path

from . import views

app_name = 'adminPanel'

urlpatterns = [
    path('admin-panel/', views.admin_Panel, name='admin_Panel'),
    path('setInterview', views.setInterview, name='setInterview'),
    path('checkInterview', views.checkInterview, name='checkInterview')
]