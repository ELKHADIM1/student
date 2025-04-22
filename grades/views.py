from django.shortcuts import render
from .models import Grade

def home(request):
    error = None
    student_grades = None
    if request.method == 'POST':
        apogee = request.POST.get('apogee')
        cin = request.POST.get('cin')
        student_grades = Grade.objects.filter(apogee=apogee, cin=cin)
        if not student_grades.exists():
            error = "لم يتم العثور على معلومات الطالب. تحقق من المعطيات."
    return render(request, 'home.html', {'grades': student_grades, 'error': error})