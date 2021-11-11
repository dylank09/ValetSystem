from django.db import models


class Valet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def getName(self):
        return self.name
