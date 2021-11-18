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
