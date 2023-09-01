from django.urls import path
from book.views import home ,store_book,show_books


urlpatterns = [
    path('' , home , name= 'homepage'),
    path('store_book_file/', store_book , name= 'storebook'),
    path('show_book_file/' , show_books , name= 'showbook'),
]