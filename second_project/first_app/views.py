from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contact(request):
    return HttpResponse('''
                        <h1> This is contact page of Django</h1>
                        <a href = '/first_app/about/'>About</a>
                        ''')

def about(request):
    return HttpResponse('''
                        <h1> This is about page of Django</h1>
                        <a href = '/first_app/contact/'>Contact</a>
                        ''')
