from django.db import models


class User(models.Model):
    name = models.CharField(max_length=28, default="customer")
    surename = models.CharField(max_length=28, default="surename")
    password = models.CharField(max_length=50, default="abc123")
    email = models.CharField(max_length=50, default="customer@gmail.com")

    class Meta:
        abstract = True
