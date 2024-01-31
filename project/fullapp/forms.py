from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class SignUpFormPart2(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name',)

# class SignUpFormPart2(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('options')

class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
