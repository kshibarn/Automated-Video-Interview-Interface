from django.shortcuts import render, redirect
from .models import Set_Interview, Check_Interview

# Create your views here.

def admin_Panel(request):
    return render(request, "AdminPanel.html")

def setInterview(request):
    set_interview = Set_Interview.objects.first()
    
    return render(request, "AdminPanel/SetInterview.html", {'set_interview': set_interview})

def checkInterview(request):
    check_interview = Check_Interview.objects.all()

    return render(request, "AdminPanel/CheckInterview.html", {'check_interview': check_interview})