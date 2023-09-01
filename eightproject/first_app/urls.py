from django.urls import path
from .views import home , singup , Login , profile , user_logout , pass_change , pass_change2 , change_user_data

urlpatterns = [
    path('' , home , name = 'homepage'),
    path('singup/' , singup , name = 'singuppage'),
    path('login/' , Login , name = 'loginpage'),
    path('profile/' , profile , name = 'profilepage'),
    path('logout/' , user_logout , name = 'logoutpage'),
    path('pass_change/' , pass_change , name = 'passchange'),
    path('passchange2/' , pass_change2 , name = 'passchange2'),
    path('change_user_data/' , change_user_data , name = 'changeuserdata'),
]