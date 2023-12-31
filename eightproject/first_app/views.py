from django.shortcuts import render , redirect
from .forms import RegistrationForm , ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm , SetPasswordForm
from django.contrib.auth import authenticate , login , logout , update_session_auth_hash
# Create your views here.

def home(request):
    return render(request , 'home.html')

def singup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request , 'Account is created successfully')
                print(form.cleaned_data)
        else:
            form=RegistrationForm()
        return render(request , 'singup.html',{'form':form})
    else:
        return redirect('profilepage')

def Login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request , data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name , password = userpass)
                if user is not None:
                    login(request , user)
                    return redirect('profilepage')
        else:
            form = AuthenticationForm()
        return render(request , './login.html',{'form':form})
    else:
        return redirect('profilepage')
    
def profile(request):
    # if request.user.is_authenticated:
    #     return render(request , './profile.html' ,{'user':request.user})
    # else:
    #     return redirect('loginpage')
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ChangeUserData(request.POST , instance = request.user)
            if form.is_valid():
                form.save()
                messages.success(request , 'Account update successfully')
        else:
            form=ChangeUserData()
        return render(request , 'profile.html',{'form':form})
    else:
        return redirect('singuppage')

def user_logout(request):
    logout(request)
    return redirect('loginpage')

def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user = request.user , data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request , form.user)
            return redirect('profilepage')
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request , './passchange.html', {'form':form})

def pass_change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(user = request.user , data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request , form.user)
            return redirect('profilepage')
    else:
        form = SetPasswordForm(user = request.user)
    return render(request , './passchange.html', {'form':form})


def change_user_data(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = ChangeUserData(request.POST , instance = request.user)
            if form.is_valid():
                form.save()
                messages.success(request , 'Account update successfully')
        else:
            form=ChangeUserData(instance = request.user)
        return render(request , 'profile.html',{'form':form})
    else:
        return redirect('singuppage')

