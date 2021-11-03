from django.db import models

from .users.customer import Customer
from .valetservice import ValetService

class Booking(models.Model):
    #bookingNumber = models.CharField(default = random_string)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    valetservice = models.ForeignKey(ValetService, on_delete=models.CASCADE)
    carReg = models.DecimalField(max_digits=20, decimal_places=15)



    def __str__(self):
        return f'{self.user} has booked {self.start_time} until {self.end_time}'