from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, SignInForm


def index(request):
    if request.user.is_authenticated:
        return render(request, 'authenticatedUser.html')
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'auth/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = SignInForm()
    return render(request, 'auth/signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('home')

# def createCategory():
    