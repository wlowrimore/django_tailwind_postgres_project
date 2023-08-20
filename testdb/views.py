from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You are now logged out.')
    return redirect('home')