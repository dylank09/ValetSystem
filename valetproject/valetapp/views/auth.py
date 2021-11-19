from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from ..Userfactory import Userfactory
from ..forms.signup import SignUpForm
from django.contrib.auth import authenticate, login as auth_login


# from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=username, password=password)
            if user:
                if user.is_active:
                    auth_login(request, user)
            return redirect('../home/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('../home/')
        

def register(request):
    if request.method == 'POST':
        factory = Userfactory
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            factory.createuser(factory, form, user)
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})