from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponse
from django.views.decorators import gzip
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseServerError


import cv2

# Create your views here.

def home(request):
    return render(request, "index.html")

def interviewList(request):
    return render(request, "InterviewList.html")

def interview(request):
    return render(request, "MainInterview.html")

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Define the function to generate frames
@gzip.gzip_page
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# Decorate the view with gzip compression to improve performance
@csrf_exempt
def video_1(request):
    try:
        return StreamingHttpResponse(gen(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')
    except:
        return HttpResponse("An error occurred")