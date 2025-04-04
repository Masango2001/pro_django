from django import forms
from .models import User, Student
from django.forms import TextInput, EmailInput, NumberInput

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'email', 'age']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'surname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'age': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Âge'}),
        }