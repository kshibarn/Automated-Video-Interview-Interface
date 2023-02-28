from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):

    # If request method is POST, attempt to create a new user
    if request.method == 'POST':

        # Extract relevant form data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['signpass']
        password2 = request.POST['confirmpass']
        email = request.POST['email']

        # # If password1 and password2 match, attempt to create a new user
        if password1 == password2:

            # If the username is already taken, redirect to register page with an error message
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            
            # If the email is already taken, redirect to register page with an error message
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            
            # Create a new user with the provided data and redirect to login page
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')

        # If password1 and password2 do not match, redirect to register page
        else:
            messages.info(request, 'Password not matching..')
            return redirect('register')

        return redirect('/')
    
    # If request method is not POST, render the register page
    else:
        return render(request, "register.html")