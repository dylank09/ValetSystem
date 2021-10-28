from django.shortcuts import render, redirect

from django.http import HttpResponse

from .forms.signup import SignUpForm

from .models import ChainStore

from django.contrib.auth import login


def index(request):
    return HttpResponse("Hello, world!")


def chainstore_by_id(request, chainstore_id):
    chainStore = ChainStore.objects.get(pk=chainstore_id)
    return render(request, 'chainstore_details.html', {'chainStore': chainStore})


def bookingscreen(request, ):
    return render(request, 'bookingscreen.html')


def register(request, ):

    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, "register.html", {"form": form})


def homescreen(request, ):
    return render(request, "homescreen.html")


def home(request, ):
    return render(request, 'home.html')
