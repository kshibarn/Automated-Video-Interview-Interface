from django.shortcuts import render

# Create your views here.

def admin(request):
    return render(request, "AdminPanel.html")

def setInterview(request):
    return render(request, "SetInterview.html")

def checkInterview(request):
    return render(request, "CheckInterview.html")