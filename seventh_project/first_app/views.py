from django.shortcuts import render
from first_app.forms import StudentForm
from first_app.models import Teacher,Student
# Create your views here.

def home(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form=StudentForm()
    return render(request, 'home.html' , {'Form' : form})

def showData(request):
    # #teacher list for one student
    # teacher = Teacher.objects.get(name = 'Shah Alam')
    # student= teacher.student.all()
    # for stud in student:
    #     print(stud.name)
    
    #student list for one teacher
    student = Student.objects.get(name = 'Rana')
    teachers= student.teachers.all()
    for teac in teachers:
        print(teac.name)
    
    return render(request,'show_data.html')
