from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse, request

from ..forms.signup import SignUpForm
from ..forms.login import LoginForm
from ..models import ChainStore
from ..models import Booking, ValetService
from ..forms.bookService import AvailabilityForm
from ..booking_functions.availability import check_availability
from ..Userfactory import Userfactory

#from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from django.views.generic import ListView, FormView

import datetime

from django.contrib.auth import login


def index(request):
    return HttpResponse("Hello, world!")


def chainstore_by_id(request, chainstore_id):
    chainStore = ChainStore.objects.get(pk=chainstore_id)
    return render(request, 'chainstore_details.html', {'chainStore': chainStore})


def bookingscreen(request):
    return render(request, 'bookingscreen.html')


class BookingList(ListView):
    model = Booking
    context_object_name = 'obj'
    template_name = 'booking_list.html'


class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'bookingservice_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        booking_list = ValetService.objects.filter(
            valetType=data['valet_categories'])
        available_booking = []
        for valetservice in booking_list:
            if check_availability(valetservice, data['start_time'], data['end_time']):
                available_booking.append(valetservice)
        if len(available_booking) > 0:
            valetservice = available_booking[0]
            valetservice = Booking.objects.create(
                user=request.user,
                valetservice=valetservice,
                start_time=data['start_time'],
                end_time=data['end_time']
            )
            valetservice.save()
            return HttpResponse(valetservice)
        else:
            return HttpResponse('This booking is already booked sorry pal')


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
def loginUser(request):

    next = request.GET.get('next')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }

    return render(request, "login.html", context)
