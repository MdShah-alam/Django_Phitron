from django.shortcuts import render,redirect
from .forms import BookStoreForm
from .models import BookStoreModel

# Create your views here.
def home(request):
    return render(request , 'base.html')

def store_book(request):
    if request.method == 'POST':
        book = BookStoreForm(data=request.POST)
        if book.is_valid():
            print('HI')
            print(book.changed_data)
            book.save(commit=False)
            # redirect 'show_books'
    else:
        book = BookStoreForm()
        print('H')
    return render(request , 'store_book.html',{'form':book})

def show_books(request):
    book = BookStoreModel.objects.all()
    print(book)
    return render(request , 'show_book.html',{'data':book})