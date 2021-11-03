from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
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

import datetime

from django.contrib.auth import login


def index(request):
    return HttpResponse("Hello, world!")


def chainstore_by_id(request, chainstore_id):
    chainStore = ChainStore.objects.get(pk=chainstore_id)
    return render(request, 'chainstore_details.html', {'chainStore': chainStore})


def bookingscreen(request):
    return render(request, 'bookingscreen.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def selecttime(request, ):

    #context = super(selecttime, self).get_context_data(**kwargs)
    start_time = '9:00'
    end_time = '18:00'
    slot_time = 60

    arrayOfDays = ["monday", "tuesday", "wenesday",
                   "thursday", "friday", "Saturday"]
    # Start date from today to next 5 day
    start_date = datetime.datetime.now().date()
    end_date = datetime.datetime.now().date() + datetime.timedelta(days=5)

    days = []
    date = start_date
    while date <= end_date:
        hours = []
        time = datetime.datetime.strptime(start_time, '%H:%M')
        end = datetime.datetime.strptime(end_time, '%H:%M')
        while time <= end:
            hours.append(time.strftime("%H:%M"))
            time += datetime.timedelta(minutes=slot_time)
        date += datetime.timedelta(days=1)
        days.append(hours)

    i = 0
    for hours in days:
        array = [arrayOfDays[i], "-", hours]
        i = i + 1

    #context['days'] = days

    return render(request, 'selecttime.html', {'days': days})


# @login_required
def login(request, user):

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
