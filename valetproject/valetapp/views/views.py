from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse, request

from ..forms.signup import SignUpForm
from ..forms.login import LoginForm
from ..models import ChainStore
from ..models.booking import Booking
from ..models.valetservice import CompositeBaseValet, CompositeExterior, Wash, Wax, Polish, CompositeInterior, SteamClean, Hoover, Leather
from ..models.valet import Valet
from ..models.users.customer import Customer
from ..forms.bookService import AvailabilityForm
from ..booking_functions.availability import check_availability
from ..Userfactory import Userfactory
from .addOns import Concrete_Valet, WaxStatus
import time


#from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from django.views.generic import ListView, FormView

import datetime
from datetime import datetime
import pytz
from django.contrib.auth import login
utc = pytz.UTC


def index(request):
    return HttpResponse("Hello, world!")


def chainstore_by_id(request, chainstore_id):
    chainStore = ChainStore.objects.get(pk=chainstore_id)
    return render(request, 'chainstore_details.html', {'chainStore': chainStore})


class BookingList(ListView):
    model = Booking
    context_object_name = 'obj'
    template_name = 'booking_list.html'





def bookingCreate(request):
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            valetSelected = data['valet_services']
            available_booking = []
            for valet in valetSelected:
                available_booking.append(valet)
            print(available_booking)
            # for valetservice in booking_list:
            #     if check_availability(valetservice, data['start_time'], data['end_time']):
            #         available_booking.append(valetservice)
            MainComposite = CompositeBaseValet()
            Composti1 = CompositeExterior()

            for valet in available_booking:
                if(valet == "Wax"):
                    Composti1.add(Wax())
                if(valet == "Wash"):
                    Composti1.add(Wash())
                if(valet == "Polish"):
                    Composti1.add(Polish())

            Composti2 = CompositeInterior()
            MainComposite.add(Composti1)
            MainComposite.add(Composti2)
            bookingDuration = MainComposite.addDuration()
            bookingDuration = datetime.timedelta(minutes=bookingDuration)
            print(bookingDuration)
            if len(available_booking) > 0:
                print("ID", request.user.id)
                valetservice2 = available_booking[0]
                booking = Booking(
                    user=Customer.objects.filter(user=request.user)[0],
                    valetservice=Valet.objects.filter(name=valetservice2)[0],
                    start_time=data['start_time'],
                    end_time=data['start_time'] + bookingDuration
                )
                print(booking)
                booking.save()
            return redirect('home')
    else:
        form = AvailabilityForm()
    return render(request, 'bookingservice_form.html', {'form': form})


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
    Wax1 = Wax()
    Wash1 = Wash()
    Polish1 = Polish()

    Hoover1 = Hoover()
    SteamClean1 = SteamClean()
    Leather1 = Leather()

    MainComposite = CompositeBaseValet()
    Composti1 = CompositeExterior()
    Composti1.add(Wax1)
    Composti1.add(Wash1)

    Composti1.add(Polish1)

    Composti2 = CompositeInterior()
    Composti2.add(Hoover1)
    Composti2.add(SteamClean1)

    Composti2.add(Leather1)
    MainComposite.add(Composti1)
    MainComposite.add(Composti2)
    MainComposite.addDuration()
    return render(request, 'home.html')


def selecttime(request, ):

    #context = super(selecttime, self).get_context_data(**kwargs)
    start_time = '9:00'
    end_time = '18:00'
    slot_time = 60

    arrayOfDays = ["monday", "tuesday", "Wednesday",
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


def viewBooking(request, bookingId):
    booking = Booking.objects.get(pk=bookingId)
    print(booking.valetservice)
    datetimeToday = datetime.now().replace(tzinfo=utc)
    hasBookingStarted = 'Booking has not started yet'
    if booking.start_time <= datetimeToday.replace(tzinfo=utc):
        hasBookingStarted = ""
        baseValet = Concrete_Valet()
        print(baseValet.getValetStatus())
        print(booking.valetservice.getName())
        if booking.valetservice.getName() == 'Wax':
            print("Hello")
            baseValet = WaxStatus(baseValet)
            print(baseValet.getValetStatus())
            Wax1 = Wax()
            print(Wax1.addDuration())
            time.sleep(Wax1.addDuration())
            print(baseValet.getValetStatusEnd())
    else:
        pass
    booking = {
        'booking': booking,
        'hasBookingStarted': hasBookingStarted
    }
    return render(request, "bookingView.html", {'booking': booking})
