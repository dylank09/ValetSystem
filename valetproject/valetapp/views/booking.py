from django.shortcuts import render
from ..models import ChainStore
from ..models.booking import Booking
from ..models.valetservice import CompositeBaseValet, CompositeExterior, Wash, Wax, Polish, CompositeInterior, SteamClean, Vacuum, Leather
from ..models.users.customer import Customer
from ..forms.bookService import AvailabilityForm
from .addOns import ConcreteValet, WaxCost, WashCost, PolishCost, LeatherCost, SteamCleanCost, VacuumCost
import math
from datetime import datetime, timedelta
import pytz

utc=pytz.UTC

from django.views.generic import ListView


class BookingList(ListView):
    model = Booking
    context_object_name = 'obj'
    template_name = 'booking_list.html'


def closest_avail_store(store, long, lat, start_time, stores_to_exclude):

    stores = ChainStore.objects.exclude(name=store)
    for store2 in stores_to_exclude:
        stores = stores.exclude(name=store2)

    closest_store = stores[0]

    X = closest_store.get_longitude() - long
    Y = closest_store.get_latitude() - lat

    closest_store_distance = distance_to_store(X, Y)

    for store in stores:
        X = store.get_longitude() - long
        Y = store.get_latitude() - lat
        distance_to_current = distance_to_store(X, Y)

        if(distance_to_current < closest_store_distance):
            closest_store = store

    store_max = closest_store.get_max_valets_per_hour()
    storeid = ChainStore.objects.filter(name=closest_store.get_name())[0]

    bookings = Booking.objects.filter(store=storeid, start_time=start_time)

    if (len(bookings) <= store_max):
        return closest_store

    stores_to_exclude.append(closest_store)
    return closest_avail_store(
        store, X, Y, start_time, stores_to_exclude)


def distance_to_store(x, y):
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))


def check_booking_availability(store_name, storeid, start_time):

    store = ChainStore.objects.get(name=store_name)
    store_max = store.get_max_valets_per_hour()

    bookings = Booking.objects.filter(store=storeid, start_time=start_time)

    store_long = store.get_longitude()
    store_lat = store.get_latitude()

    if (len(bookings) > store_max):

        stores_to_exclude = [store]
        tempstore = closest_avail_store(
            store, store_long, store_lat, start_time, stores_to_exclude)
        return tempstore
    else:
        return store


def init_booking_form(request):
    if request.method != 'POST':
        form = AvailabilityForm()
        return render(request, 'bookingservice_form.html', {'form': form})

    form = AvailabilityForm(request.POST)

    if form.is_valid():
        data = form.cleaned_data
        return create_booking(request, data)


def create_booking(request, data):

    available_booking = data['valet_services']

    base, total_booking_cost, valets = get_valet_services(available_booking)

    booking_duration = base.add_duration()
    booking_duration = timedelta(minutes=booking_duration)

    store_name = data['stores']
    storeid = ChainStore.objects.filter(name=data['stores'])[0]
    store = check_booking_availability(
        store_name, storeid, data['start_time'])
    storeid = ChainStore.objects.filter(name=store.get_name())[0]

    if len(available_booking) > 0:  # precondition
        return make_booking(request, data, total_booking_cost, valets, booking_duration, storeid)

    return ""


def get_valet_services(available_booking):

    base = CompositeBaseValet()
    ext_composite = CompositeExterior()
    int_composite = CompositeInterior()
    valet = ConcreteValet()
    valets = ""

    for v in available_booking:
        if v == "Leather":
            int_composite.add(Leather())
            valet = LeatherCost(valet)
        elif v == "Polish":
            ext_composite.add(Polish())
            valet = PolishCost(valet)
        elif v == "Steam":
            int_composite.add(SteamClean())
            valet = SteamCleanCost(valet)
        elif v == "Vacuum":
            int_composite.add(Vacuum())
            valet = VacuumCost(valet)
        elif v == "Wash":
            ext_composite.add(Wash())
            valet = WashCost(valet)
        elif v == "Wax":
            ext_composite.add(Wax())
            valet = WaxCost(valet)

        valets = v+","+valets

    total_booking_cost = valet.get_valet_cost()

    base.add(ext_composite)
    base.add(int_composite)

    return base, total_booking_cost, valets


def make_booking(request, data, total_booking_cost, valets, booking_duration, storeid):
    customer = Customer.objects.filter(user=request.user)[0]
    booking = Booking(
        user=customer,
        valetservice=valets,
        start_time=data['start_time'],
        end_time=data['start_time'] + booking_duration,
        price=total_booking_cost,
        store=storeid
    )

    booking.save()
    check_for_free_8th_booking(customer, booking)
    return pay_for_booking(request, booking)


def pay_for_booking(request, booking):

    customer = Customer.objects.filter(user=request.user)[0]

    old_price = (booking.get_price())
    customer.update(booking)
    discount = old_price - booking.get_price()
    return render(request, "payForBooking.html", {'booking': booking, 'oldPrice': old_price, 'discount': discount})


def check_for_free_8th_booking(customer, booking):
    bookings = Booking.objects.filter(user=customer)
    number_of_bookings = len(bookings) % 8
    if number_of_bookings == 0:
        booking.set_price(0)
        

def confirm_pay(request, bookingid):
    booking = Booking.objects.filter(id=bookingid)[0]
    booking.book()
    booking.save()
    
    return render(request, 'home.html')


def cancel_booking(request, bookingid):
    booking = Booking.objects.filter(id=bookingid)[0]
    now = datetime.now()
    if utc.localize(now-timedelta(hours=24)) <= booking.get_start_time() <=  utc.localize(now+timedelta(hours=24)):
        print('error cannot cancel 24 hours before')
    else:
        booking.cancel()
        booking.save()

    print(booking.get_booking_status())
    return render(request, 'home.html')


def view_user_bookings(request):
    customer = Customer.objects.filter(user=request.user)[0]
    bookings = Booking.objects.filter(user=customer)
    bookings = bookings.exclude(booking_state="CANCELLED")
    bookingID = []
    for booking in bookings:
        bookingID.append(booking.id)
    return render(request, 'cancel_list.html', {'bookings': bookings, 'bookingID': bookingID})
