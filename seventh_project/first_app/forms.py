from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields = '__all__'
        
        labels = {
            'name' : 'Student name',
            'roll' : 'student roll'
        }
        
        help_taxts = {
            'roll' : "write your name"
        }