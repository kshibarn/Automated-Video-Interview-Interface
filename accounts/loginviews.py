from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.urls import reverse

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        # If the user exists, log the user in and redirect to home page
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        
        elif user is not None and user.is_superuser:
            # Redirect to custom admin panel
            return redirect(reverse('adminPanel:admin_Panel'))
        
        # If the user does not exist, display an error message and redirect to login page
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    
    # If request method is not POST, render the login page
    else:
        return render(request, "login.html")
    
def logout(request):

    # Log the user out and redirect to home page
    auth.logout(request)
    return redirect('/')