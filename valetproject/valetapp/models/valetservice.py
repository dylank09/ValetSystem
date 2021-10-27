from django.db import models

class ValetService(models.Model):
    valetType = models.CharField(max_length=100)