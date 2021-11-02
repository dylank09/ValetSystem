from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms.signup import SignUpForm
from .forms.login import LoginForm
from .models import ChainStore
#from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)



def index(request):
    return HttpResponse("Hello, world!")


def chainstore_by_id(request, chainstore_id):
    chainStore = ChainStore.objects.get(pk=chainstore_id)
    return render(request, 'chainstore_details.html', {'chainStore': chainStore})


def bookingscreen(request):
    return render(request, 'bookingscreen.html')


def register(request):

    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, "register.html", {"form": form})


def home(request):
    return render(request, 'home.html')

#@login_required
def login(request):

    next = request.GET.get('next')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        login(request, email)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }

    return render(request, "login.html", context)
