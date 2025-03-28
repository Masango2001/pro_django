from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . models import Student
from . form import studentForm
def home(request):
    students=Student.objects.all()
    return render(request,'index.html',{'students':students})
def service(request):
    return render(request,'service.html')
def create_student(request):
    if request.method=='POST':
        form=studentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Étudiant ajouté avec succès !')
            return redirect('home')
    else:
        form=studentForm()
    return render(request,'form.html',{'form':form})
def edit_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = studentForm(request.POST, instance=student)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Étudiant mis à jour avec succès !') 
            return redirect('home')
    else:
        form = studentForm(instance=student) 

    return render(request, 'form.html', {'form': form})
   
def delete_student(request,id):
    student=get_object_or_404(Student,id=id)
    student.delete()
    messages.success(request, 'Étudiant supprimé avec succès !')
    return redirect('home')
     



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Compte créé pour {username} !')
            return redirect('login')
    else:
        form = UserCreationForm()
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
    return redirect('login')