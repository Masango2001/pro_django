from django.urls import path 
from .import views
urlpatterns=[
    path('home',views.home, name='home'),
    path('service/',views.service, name='service'),
        
    path('create/',views.create_student, name='create_student'),
    
    path('edit/<int:id>/',views.edit_student, name='edit_student'),
    path('delete/<int:id>/',views.delete_student, name='delete_student'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.register, name='register'),
    
   
]