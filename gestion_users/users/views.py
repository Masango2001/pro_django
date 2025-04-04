from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Student
from .form import StudentForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .decorators import role_required

@login_required
def home(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

@login_required
@role_required(['recteur', 'rh', 'comptable'])  # Rôles autorisés pour créer un étudiant
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Étudiant ajouté avec succès !')
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'form.html', {'form': form})

@login_required
@role_required(['recteur', 'rh', 'comptable'])  # Rôles autorisés pour éditer un étudiant
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Étudiant mis à jour avec succès !')
            return redirect('home')
    else:
        form = StudentForm(instance=student)
    return render(request, 'form.html', {'form': form})

@login_required
@role_required(['recteur', 'rh'])  # Rôles autorisés pour supprimer un étudiant
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    messages.success(request, 'Étudiant supprimé avec succès !')
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash le mot de passe
            user.save()
            messages.success(request, f'Compte créé pour {user.username} !')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'inscrire.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Identifiants invalides.')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Vous êtes déconnecté.')
    return redirect('login')