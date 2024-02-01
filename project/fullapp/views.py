from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, SignUpFormPart2, SignInForm
from django.contrib.auth.decorators import login_required


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
            return redirect('signUpPart2')
    else:
        form = SignUpForm()
    return render(request, 'auth/signup.html', {'form': form})

@login_required
def signUpPart2(request):
    if request.method == 'POST':
        form = SignUpFormPart2(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpFormPart2(instance=request.user)
    return render(request, 'auth/signupName.html', {'form': form})

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

    