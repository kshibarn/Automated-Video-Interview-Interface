from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "index.html")

def interviewList(request):
    return render(request, "InterviewList.html")

def interview(request):
    return render(request, "MainInterview.html")

def recorderWorker(request):
    return render(request, 'recorderWorker.js')

def webcamWorker(request):
    return render(request, 'webcamWorker.js')

def analyzeSpeech(request):
    return render(request, 'analyzeSpeech.html')