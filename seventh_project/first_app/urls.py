from django.urls import path
# from . import 
from first_app.views import home,showData


urlpatterns = [
    path('',home , name = "Homepage"),
    path('show/',showData, name='showData'),
]