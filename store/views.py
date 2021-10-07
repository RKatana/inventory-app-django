from django.shortcuts import render
from .models import Users
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.shortcuts import render,redirect

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password: 
            user = Users(username=username, email=email, password=make_password(password))
            user.save()
            messages.add_message(request, messages.SUCCESS, "You have successfully registered!")
            return redirect(signin)
    return render(request, 'login/signup.html')


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "You have successfully login!")
            return redirect('index')
        else:
            messages.add_message(request, messages.WARNING, "Invalid credentials!")
            return redirect('signin')
    else:
        return render(request, 'login/signin.html')