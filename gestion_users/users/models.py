from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    age=models.IntegerField()
    
    class  Meta:
        db_table = 'project_django'
        
        
