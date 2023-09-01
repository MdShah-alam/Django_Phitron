from django import forms
from .models import BookStoreModel

class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStoreModel
        # fields='__all__'
        exclude = ['first_pub' , 'last_pub']