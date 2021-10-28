from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=28)
    surname = models.CharField(max_length=28)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        abstract = True
