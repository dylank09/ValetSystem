from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from valetapp.views.concreteVisitor import ConcreteVisitor

from valetapp.views.visitor import Visitor
from .concreteVisitor import ConcreteVisitor

from ..forms.signup import SignUpForm
# from ..forms.login import LoginForm
from ..models import ChainStore
from ..models.booking import Booking
from ..models.valetservice import CompositeBaseValet, CompositeExterior, Wash, Wax, Polish, CompositeInterior, SteamClean, Vacuum, Leather
from ..models.valet import Valet
from ..models.users.customer import Customer
from ..models.users.membershiptype import MembershipType
from ..models.users.staff import Staff
from ..forms.bookService import AvailabilityForm
from ..booking_functions.availability import check_availability
from ..Userfactory import Userfactory
from .addOns import Concrete_Valet, WaxCost, WashCost, PolishCost, LeatherCost, SteamCleanCost, VacuumCost
import time
import math


# from django.contrib.auth.decorators import login_required
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


class BookingList(ListView):
    model = Booking
    context_object_name = 'obj'
    template_name = 'booking_list.html'


def payForBooking(request, bookingId):
    booking = Booking.objects.get(pk=bookingId)
    
    customer= Customer.objects.filter(user=request.user)[0]

    oldPrice = (booking.getPrice())
    customer.update(booking)
    discount = oldPrice - booking.getPrice()
    return render(request, "payForBooking.html", {'booking':booking, 'oldPrice': oldPrice, 'discount':discount})

def getVisitor(request):
    bookings = Booking.objects.all()
    customers = Customer.objects.all()
    stores = ChainStore.objects.all()
    valets = Valet.objects.all()
    membershipTypes = MembershipType.objects.all()
    staffs = Staff.objects.all()
    print(customers)
    print(bookings)
    visitor = ConcreteVisitor()
    sum = 0
    for booking in bookings:
        sum += booking.accept(visitor)
    for customer in customers:
        print(customer.accept(visitor))
    for store in stores:
        print(store.accept(visitor))
    for valet in valets:
        print(valet.accept(visitor))
    for membershipType in membershipTypes:
        print(membershipType.accept(visitor))
    for staff in staffs:
        print(staff.accept(visitor))
    print(sum)
    return render(request, "booking_list.html")


def getClosestStoreWithAvailableTime(store, long, lat, storeID, startTime, storesToExclude):
    print("Hello")
    print("Stores to exlucde: ", storesToExclude)
    stores = ChainStore.objects.exclude(name=store)
    for store2 in storesToExclude:
        print(store2)
        stores = stores.exclude(name=store2)
    print("B: ", stores)
    print(long)
    print(lat)
    # stores = [store.getName() for valet in valetObjects]
    closestStore = stores[0]
    X = closestStore.getLongitude() - long
    Y = closestStore.getLatitude() - lat
    closestStoreDistanceToCurrentStore = math.sqrt(
        math.pow(X, 2) + math.pow(Y, 2))
    print(stores)
    # stores = stores.exclude(name=closestStore.getName())
    print(stores)
    # VALET_CATERGORIES = [(valet, valet.getName()) for valet in valetObjects]
    for store in stores:
        X = store.getLongitude() - long
        Y = store.getLatitude() - lat
        distanceToCurrentStore = math.sqrt(math.pow(X, 2) + math.pow(Y, 2))
        print(distanceToCurrentStore)
        if(distanceToCurrentStore < closestStoreDistanceToCurrentStore):
            closestStore = store
    print(closestStore)

    storeMax = closestStore.getMaxNumberOfValetsPerHour()
    storeID = ChainStore.objects.filter(name=closestStore.getName())[0]
    bookings = Booking.objects.filter(store=storeID, start_time=startTime)
    if(len(bookings) <= storeMax):
        print("Hello")
        print(closestStore)
        return closestStore
    else:
        storesToExclude.append(closestStore)
        return getClosestStoreWithAvailableTime(
            store, X, Y, storeID, startTime, storesToExclude)


def checkBookingAvailability(storeName, storeID, startTime):
    store = ChainStore.objects.get(name=storeName)
    storeMax = store.getMaxNumberOfValetsPerHour()
    bookings = Booking.objects.filter(store=storeID, start_time=startTime)

    print(len(bookings))
    print(storeMax)
    print(startTime)
    storeLongititude = store.getLongitude()
    storeLatitude = store.getLatitude()
    if(len(bookings) > storeMax):
        print("Hello")
        storesToExclude = []
        storesToExclude.append(store)
        print("A: ", storesToExclude)
        tempstore = getClosestStoreWithAvailableTime(
            store, storeLongititude, storeLatitude, storeID, startTime, storesToExclude)
        print(tempstore)
        return tempstore
    else:
        return store


def bookingCreate(request):
    if request.method != 'POST':
        form = AvailabilityForm()

    else:
        form = AvailabilityForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data
            valetSelected = data['valet_services']
            available_booking = [valet for valet in valetSelected]

            print(available_booking)

            MainComposite = CompositeBaseValet()
            Composti1 = CompositeExterior()
            Composti2 = CompositeInterior()
            baseValet = Concrete_Valet()
            totalBookingCost = 0
            valets = ""

            for valet in available_booking:
                if valet == "Leather":
                    Composti2.add(Leather())
                    baseValet = LeatherCost(baseValet)
                elif valet == "Polish":
                    Composti1.add(Polish())
                    baseValet = PolishCost(baseValet)
                elif valet == "Steam":
                    Composti2.add(SteamClean())
                    baseValet = SteamCleanCost(baseValet)
                elif valet == "Vacuum":
                    Composti2.add(Vacuum())
                    baseValet = VacuumCost(baseValet)
                elif valet == "Wash":
                    Composti1.add(Wash())
                    baseValet = WashCost(baseValet)
                elif valet == "Wax":
                    Composti1.add(Wax())
                    baseValet = WaxCost(baseValet)

                valets = valet+","+valets

            totalBookingCost = baseValet.getValetCost()

            MainComposite.add(Composti1)
            MainComposite.add(Composti2)
            bookingDuration = MainComposite.addDuration()
            bookingDuration = timedelta(minutes=bookingDuration)
            storeName = data['stores']
            storeID = ChainStore.objects.filter(name=data['stores'])[0]
            store = checkBookingAvailability(
                storeName, storeID, data['start_time'])
            print("Temp", store)
            storeID = ChainStore.objects.filter(name=store.getName())[0]
            print(bookingDuration)
            print(data['start_time'])
            print(data['start_time'] + bookingDuration)

            return makeBooking(request, data, available_booking, totalBookingCost, valets, bookingDuration, storeID)
            
            # return redirect('home')

    return render(request, 'bookingservice_form.html', {'form': form})


def makeBooking(request, data, available_booking, totalBookingCost, valets, bookingDuration, storeID):
    if len(available_booking) > 0:
        booking = Booking(
            user=Customer.objects.filter(user=request.user)[0],
            valetservice=valets,
            start_time=data['start_time'],
            end_time=data['start_time'] + bookingDuration,
            price=totalBookingCost,
            store=storeID
        )
        print(booking)
        booking.save()
        print(booking.id)
        # render(request, 'payForBooking.html', {'bookingID': booking.id})
        
        return payForBooking(request, booking.id)



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


def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('../home/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
