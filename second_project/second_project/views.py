from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> Hello Shah_Alam this is your first web page </h1>")