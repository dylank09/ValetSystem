from django.db import models


class ChainStore(models.Model):
    name = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=20, decimal_places=15)
    latitude = models.DecimalField(max_digits=20, decimal_places=15)
    rating = models.IntegerField(default=0)
    maxNumberOfValetsPerHour = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def getName(self):
        return self.name

    def getMaxNumberOfValetsPerHour(self):
        return self.maxNumberOfValetsPerHour

    def getLongitude(self):
        return self.longitude

    def getLatitude(self):
        return self.latitude
