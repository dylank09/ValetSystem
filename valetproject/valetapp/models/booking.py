from django.db import models
from .valetservice import ValetService

class Booking(models.Model):
    valetservice = models.ForeignKey(ValetService, on_delete=models.CASCADE)
    carReg = models.DecimalField(max_digits=20, decimal_places=15)