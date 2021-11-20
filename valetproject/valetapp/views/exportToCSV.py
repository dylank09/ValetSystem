from ..models.booking import Booking
from ..models.users.customer import Customer
from ..models.chainstore import ChainStore
from ..models.valet import Valet
from ..models.users.membershiptype import MembershipType
from ..models.users.staff import Staff
from .concreteVisitor import ConcreteVisitor
from django.shortcuts import render


def getVisitor(request):
    bookings = Booking.objects.all()
    customers = Customer.objects.all()
    stores = ChainStore.objects.all()
    valets = Valet.objects.all()
    membershipTypes = MembershipType.objects.all()
    staffs = Staff.objects.all()
    visitor = ConcreteVisitor()

    total_sum = 0
    customer_emails_for_promotions = []
    store_names = []
    valet_types = []
    membership_types = []
    staff_members = []

    for booking in bookings:
        total_sum += booking.accept(visitor)
    for customer in customers:
        customer_emails_for_promotions.append(customer.accept(visitor))
    for store in stores:
        store_names.append(store.accept(visitor))
    for valet in valets:
        valet_types.append(valet.accept(visitor))
    for membershipType in membershipTypes:
        membership_types.append(membershipType.accept(visitor))
    for staff in staffs:
        staff_members.append(staff.accept(visitor))

    money_made_by_each_store = get_money_made_by_each_store(bookings, stores)

    export_to_CSV_object = {
        'total_sum': total_sum,
        'customers': customer_emails_for_promotions,
        'store_names': store_names,
        'valet_types': valet_types,
        'membership_types': membership_types,
        'staff_members': staff_members,
        'money_made_by_each_store': money_made_by_each_store
    }

    return render(request, "booking_list.html", {'export_data': export_to_CSV_object})


def get_money_made_by_each_store(bookings, stores):
    money_made_by_store = []
    for store in stores:
        store_total = 0
        for booking in bookings:
            if(booking.getStore() == store):
                store_total += booking.get_price()
        money_made_by_store.append((store.get_name(), store_total))
    return money_made_by_store
