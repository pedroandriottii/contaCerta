from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, SignUpFormPart2, SignInForm, CategoryForm, TransactionForm
from django.contrib.auth.decorators import login_required
from .models import Category, Transaction
from django.db.models import Sum

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

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'categories/categoryList.html', {'categories': categories})

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'categories/categoryCreate.html', {'form': form})

@login_required
def TransactionList(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'transactions/transactionList.html', {'transactions': transactions})

@login_required
def CreateTransaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('TransactionList')
    else:
        user_categories = Category.objects.filter(user=request.user).exclude(title='Total')
        form = TransactionForm()
        form.fields['category'].queryset = user_categories
    return render(request, 'transactions/createTransaction.html', {'form': form})

@login_required
def CategoryTotalSpent(request):
    categories = Category.objects.filter(user=request.user)
    category_totals = {}

    total_spent_all = Transaction.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0
    category_totals['Total'] = total_spent_all
    
    for category in categories:
        total_spent = Transaction.objects.filter(user=request.user, category=category).aggregate(Sum('amount'))['amount__sum'] or 0
        category_totals[category.title] = total_spent
    
    return render(request, 'transactions/categoryTotalSpent.html', {'category_totals': category_totals})