from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courses(request):
    return HttpResponse("From course page of Django")

def feedback(request):
    return HttpResponse("From feedback page of Django")
