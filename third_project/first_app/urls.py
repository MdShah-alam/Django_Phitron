from django.urls import path
from . import views

urlpatterns = [
    path('contact/',views.contact),
    path('first_app/',views.contact),
]