from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=28)
    surname = models.CharField(max_length=28)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f'Name: {self.firstname} {self.surname}'

    class Meta:
        abstract = True

