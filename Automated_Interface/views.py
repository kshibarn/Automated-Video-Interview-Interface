from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators import gzip

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
def gen_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Convert the frame to bytes
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            # Yield the frame as an HTTP response
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

# Decorate the view with gzip compression to improve performance
@gzip.gzip_page
def video_feed(request):
    try:
        return HttpResponse(gen_frames(), content_type='multipart/x-mixed-replace; boundary=frame')
    except Exception as e:
        print(e)