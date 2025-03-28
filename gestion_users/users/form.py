from django import forms
from .models import Student
from django.forms import TextInput, EmailInput, NumberInput
class studentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','surname','email','age']  
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'surname': TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'age': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Âge'}),
        }