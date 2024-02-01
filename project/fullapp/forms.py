from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Category, Transaction

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class SignUpFormPart2(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name',)

# class SignUpFormPart3(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('options')

class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['category', 'amount']

    def __init__(self, *args, **kwargs):
        user_categories = kwargs.pop('user_categories', None)
        super(TransactionForm, self).__init__(*args, **kwargs)
        if user_categories:
            self.fields['category'].queryset = user_categories
