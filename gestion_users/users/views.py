from django.shortcuts import render,redirect,get_object_or_404
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
            return redirect('home')
    else:
        form = studentForm(instance=student) 

    return render(request, 'form.html', {'form': form})
   
def delete_student(request,id):
    student=get_object_or_404(Student,id=id)
    if request.method=='POST':
        student.delete()
        return redirect('home')
    return render(request,'index.html',{'student':student}) 