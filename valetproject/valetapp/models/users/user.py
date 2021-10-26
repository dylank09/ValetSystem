from django.db import models


class User(models.Model):
    name = models.CharField(max_length=28)
    surename = models.CharField(max_length=28)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
