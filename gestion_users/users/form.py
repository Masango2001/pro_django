from django import forms
from .models import Student
class studentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','surname','email','age']  