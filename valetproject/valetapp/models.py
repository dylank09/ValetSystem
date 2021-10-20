from django.db import models

class ChainStore(models.Model):
    name = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=20, decimal_places=15)
    latitude = models.DecimalField(max_digits=20, decimal_places=15)
    # storeManager
    rating = models.IntegerField(default=0)
    status = models.BooleanField(default=True)