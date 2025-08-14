from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages



def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Account created successfully!')
            return redirect('login')  # name from urls.py
    return render(request, 'users/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')  # name from urls.py
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'users/login.html')