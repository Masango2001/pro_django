        
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    ROLE_CHOICES = [
        ('recteur', 'Recteur'),
        ('comptable', 'Comptable'),
        ('rh', 'Ressources Humaines'),
        ('technique', 'Technique'),
        ('qualite', 'Qualité'),
        ('doyen', 'Doyen'),
        ('academique', 'Académique'),
        ('employe', 'Employé'),
        ('etudiant', 'Etudiant'),
        ('enseignants', 'Eseignants'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employe')

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Changez ici pour éviter les conflits
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Changez ici pour éviter les conflits
        blank=True,
    )

    def __str__(self):
        return self.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)  # Lien avec le modèle User
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()

    class Meta:
        db_table = 'Student'

    def __str__(self):
        return f"{self.name} {self.surname}"