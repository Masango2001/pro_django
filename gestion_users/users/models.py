from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    age=models.IntegerField()
    
    def _str_(self):
        return f"{self.name} {self.surname}"
