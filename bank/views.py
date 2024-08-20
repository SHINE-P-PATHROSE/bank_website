from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm, AccountForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout as auth_logout

def home(request):
    return render(request, 'bank1/home.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'bank1/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Registration successful. Please log in.')
                return redirect('login')
            else:
                form.add_error('confirm_password', 'Passwords do not match')
    else:
        form = RegisterForm()
    return render(request, 'bank1/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'bank1/dashboard.html')

@login_required
def account_form(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
            messages.success(request, 'Application accepted')
            return redirect('dashboard')
    else:
        form = AccountForm()
    return render(request, 'bank1/account_form.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('login')
