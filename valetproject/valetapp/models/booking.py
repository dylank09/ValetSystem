from django.db import models
from enum import Enum
from .users.customer import Customer
from .valetservice import ValetService

class BookingStates(Enum):
    PENDING = 'pending'
    BOOKED =  'booked'
    CANCELLED = 'cancelled'
    END_TIME = 'endtime'

    @classmethod
    def tuples(cls): return tuple((state.name, state.value) for state in cls)


class Booking(models.Model):
    #bookingNumber = models.CharField(default = random_string)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    booking_state = models.CharField(max_length=20, choices=BookingStates.tuples(), default= BookingStates.PENDING)
    valetservice = models.ForeignKey(ValetService, on_delete=models.CASCADE)
    carReg = models.DecimalField(max_digits=20, decimal_places=15)

    def book(self): self.booking_state = BookingStates.BOOKED

    def cancel(self): self.booking_state = BookingStates.CANCELLED

    def endtime(self): self.booking_state = BookingStates.END_TIME

    def __str__(self):
        return f'{self.user} has booked {self.start_time} until {self.end_time}'


    