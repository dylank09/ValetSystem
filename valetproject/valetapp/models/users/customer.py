from django.db import models
from .user import User


class Customer(User):
    # membershipType = models.ForeignKey(MembershipType)
    colour = models.CharField(max_length=23)

    class Meta:
        app_label = "customer"
