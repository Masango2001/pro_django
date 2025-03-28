from django.contrib import admin
from . models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'age')  
    search_fields = ('name', 'surname', 'email')  

    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
    
        return queryset