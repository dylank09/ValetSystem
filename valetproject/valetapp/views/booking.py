from django.shortcuts import render, redirect

from ..models import ChainStore
from ..models.booking import Booking
from ..models.valetservice import CompositeBaseValet, CompositeExterior, Wash, Wax, Polish, CompositeInterior, SteamClean, Vacuum, Leather
from ..models.users.customer import Customer
from ..forms.bookService import AvailabilityForm
from ..booking_functions.availability import check_availability
from .addOns import Concrete_Valet, WaxCost, WashCost, PolishCost, LeatherCost, SteamCleanCost, VacuumCost
import math

from datetime import timedelta

from django.views.generic import ListView

class BookingList(ListView):
    model = Booking
    context_object_name = 'obj'
    template_name = 'booking_list.html'


def payForBooking(request, booking):
    # booking = Booking.objects.get(pk=bookingId)
    # id = booking.id
    customer= Customer.objects.filter(user=request.user)[0]

    oldPrice = (booking.getPrice())
    customer.update(booking) # 
    discount = oldPrice - booking.getPrice()

    return render(request, "payForBooking.html", {'booking':booking, 'oldPrice': oldPrice, 'discount':discount})

def confirmPay(request, booking):
    booking.save()

def getClosestStoreWithAvailableTime(store, long, lat, storeID, startTime, storesToExclude):

    stores = ChainStore.objects.exclude(name=store)
    for store2 in storesToExclude:

        stores = stores.exclude(name=store2)

    closestStore = stores[0]

    X = closestStore.getLongitude() - long
    Y = closestStore.getLatitude() - lat

    closestStoreDistanceToCurrentStore = math.sqrt(
        math.pow(X, 2) + math.pow(Y, 2))

    for store in stores:
        X = store.getLongitude() - long
        Y = store.getLatitude() - lat
        distanceToCurrentStore = math.sqrt(math.pow(X, 2) + math.pow(Y, 2))

        if(distanceToCurrentStore < closestStoreDistanceToCurrentStore):
            closestStore = store

    storeMax = closestStore.getMaxNumberOfValetsPerHour()
    storeID = ChainStore.objects.filter(name=closestStore.getName())[0]

    bookings = Booking.objects.filter(store=storeID, start_time=startTime)
    
    if (len(bookings) <= storeMax):
        return closestStore

    storesToExclude.append(closestStore)
    return getClosestStoreWithAvailableTime(
        store, X, Y, storeID, startTime, storesToExclude)


def checkBookingAvailability(storeName, storeID, startTime):

    store = ChainStore.objects.get(name=storeName)
    storeMax = store.getMaxNumberOfValetsPerHour()

    bookings = Booking.objects.filter(store=storeID, start_time=startTime)

    storeLongititude = store.getLongitude()
    storeLatitude = store.getLatitude()
    if (len(bookings) > storeMax):
        
        storesToExclude = [store]
        tempstore = getClosestStoreWithAvailableTime(
            store, storeLongititude, storeLatitude, storeID, startTime, storesToExclude)
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
            storeID = ChainStore.objects.filter(name=store.getName())[0]
            

            return makeBooking(request, data, available_booking, totalBookingCost, valets, bookingDuration, storeID)

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
        
        return payForBooking(request, booking)
