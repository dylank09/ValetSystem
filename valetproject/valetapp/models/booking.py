from django.db import models
from enum import Enum
from .users.customer import Customer
from .subject import Subject
from .chainstore import ChainStore
from .item import Item


class BookingStates(Enum):
    PENDING = 'pending'
    BOOKED = 'booked'
    CANCELLED = 'cancelled'
    END_TIME = 'endtime'

    @classmethod
    def tuples(cls): return tuple((state.name, state.value) for state in cls)


class Booking(models.Model, Subject, Item):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    store = models.ForeignKey(ChainStore, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    booking_state = models.CharField(
        max_length=20, choices=BookingStates.tuples(), default=BookingStates.PENDING)
    valetservice = models.CharField(max_length=200, default="")
    price = models.FloatField(default=0.00)

    def book(self): self.booking_state = BookingStates.BOOKED

    def cancel(self): 
        self.booking_state = BookingStates.CANCELLED
        
        print(self.booking_state)
        return self.booking_state
        

    def endtime(self): self.booking_state = BookingStates.END_TIME

    def getBookingStatus(self): return self.booking_state

    def getPrice(self): return self.price

    def setPrice(self, new_price): self.price = new_price

    def __str__(self):
        return f'{self.user} has booked {self.start_time} until {self.end_time}'

    def accept(self, visitor):
        return visitor.visit(self)
