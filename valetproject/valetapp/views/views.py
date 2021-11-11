from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse, request

from ..forms.signup import SignUpForm
from ..forms.login import LoginForm
from ..models import ChainStore
from ..models.booking import Booking
from ..models.valetservice import CompositeBaseValet, CompositeExterior, Wash, Wax, Polish, CompositeInterior, SteamClean, Vacuum, Leather
from ..models.valet import Valet
from ..models.users.customer import Customer
from ..forms.bookService import AvailabilityForm
from ..booking_functions.availability import check_availability
from ..Userfactory import Userfactory
from .addOns import Concrete_Valet, WaxCost, WashCost, PolishCost ,LeatherCost, SteamCleanCost, VacuumCost
import time


#from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from django.views.generic import ListView, FormView
from datetime import datetime, timedelta
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


# def payForBooking(request, booking):
    
#     return render(request, "bookingView.html", {'booking': booking})


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
            
            MainComposite = CompositeBaseValet()
            Composti1 = CompositeExterior()
            Composti2 = CompositeInterior()
            baseValet = Concrete_Valet()
            totalBookingCost = 0
            valets = ""

            for valet in available_booking:
                if(valet == "Wax"):
                    Composti1.add(Wax())
                    baseValet = WaxCost(baseValet)
                if(valet == "Wash"):
                    Composti1.add(Wash())
                    baseValet = WashCost(baseValet)
                if(valet == "Polish"):
                    Composti1.add(Polish())
                    baseValet = PolishCost(baseValet)
                if(valet == "Vacuum"):
                    Composti2.add(Vacuum())
                    baseValet = VacuumCost(baseValet)
                if(valet == "Steam"):
                    Composti2.add(SteamClean())
                    baseValet = SteamCleanCost(baseValet)
                if(valet == "Leather"):
                    Composti2.add(Leather())
                    baseValet = LeatherCost(baseValet)
                valets = valet+","+valets
            totalBookingCost = baseValet.getValetCost()

            MainComposite.add(Composti1)
            MainComposite.add(Composti2)
            bookingDuration = MainComposite.addDuration()
            bookingDuration = timedelta(minutes=bookingDuration)
            print(bookingDuration)
            print(data['start_time'])
            print(data['start_time'] + bookingDuration)
            if len(available_booking) > 0:
                booking = Booking(
                    user=Customer.objects.filter(user=request.user)[0],
                    valetservice=valets,
                    start_time=data['start_time'],
                    end_time=data['start_time'] + bookingDuration,
                    price=totalBookingCost
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

    Vacuum1 = Vacuum()
    SteamClean1 = SteamClean()
    Leather1 = Leather()

    MainComposite = CompositeBaseValet()
    Composti1 = CompositeExterior()
    Composti1.add(Wax1)
    Composti1.add(Wash1)

    Composti1.add(Polish1)

    Composti2 = CompositeInterior()
    Composti2.add(Vacuum1)
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
    services = booking.valetservice.split(',')
    datetimeToday = datetime.now().replace(tzinfo=utc)
    hasBookingStarted = 'Booking has not started yet'
    bookingObject = {
        'booking': booking,
        'hasBookingStarted': hasBookingStarted
    }
    totalBookingCost = 0
    if booking.start_time <= datetimeToday.replace(tzinfo=utc):
        hasBookingStarted = ""
        baseValet = Concrete_Valet()
        for service in services:
            if service == 'Wax':
                baseValet = WaxCost(baseValet)
            if service == 'Wash':
                baseValet = WashCost(baseValet)
            if service == 'Polish':
                baseValet = PolishCost(baseValet)
            if service == 'Steam':
                baseValet = SteamCleanCost(baseValet)
            if service == 'Vacuum':
                baseValet = VacuumCost(baseValet)
            if service == 'Leather':
                baseValet = LeatherCost(baseValet)
        totalBookingCost = baseValet.getValetCost()
    else:
        pass
    bookingObject['totalBookingCost'] = totalBookingCost
    return render(request, "bookingView.html", {'booking': bookingObject})
