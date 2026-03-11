from django.shortcuts import render
from .models import Students

def students_list(request):
    students = Students.objects.all()
    return render(request, 'students_list.html', {'students': students})