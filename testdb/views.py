from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import SignUpForm


def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login was successful!')
            return redirect('home')
        else:
            messages.success(request, 'There was an error with your credentials.  Please try again.')
            return redirect('home')
    else:
        return render(request, 'index.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You are now logged out.')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, 'Registration complete. You are now logged in!')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})
