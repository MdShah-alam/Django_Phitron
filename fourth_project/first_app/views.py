from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request , './first_app/home.html',{"name" : "I am Rahim", "marks" : "88" ,"courses" :
    [
        {
            "id" : 1,
            "course" : "C",
            "teacher" : "Rahm"
        },
        {
            "id" : 2,
            "course" : "C++",
            "teacher" : "karim"
        },
        {
            "id" : 3,
            "course" : "Python",
            "teacher" : "Roni"
        }
    ]})
    
def about(request):
    return render(request , './first_app/about.html',{'author' : 'glann maxwell'})