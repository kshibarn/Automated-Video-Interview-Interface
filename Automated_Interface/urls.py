from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('interviewList', views.interviewList, name='interviewList'),
    path('interview', views.interview, name='interview'),
    path('video_interview', views.video_1, name='video_1')
]