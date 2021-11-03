from django.db import models

class ValetService(models.Model):
    VALET_CATERGORIES=(
        ('WXW', 'Wax&Wash'),
        ('INW', 'Interior&Wash'),
        ('PWH', 'Polish&Wash'),
        ('ALL', 'All'),
        ('WAS', 'Wash')
    )
    valetType = models.CharField(max_length=3, choices=VALET_CATERGORIES)

    def __str__(self):
        return f'{self.valetType}'
