from django.db import models
from . import user
from .membershipType import MembershipType


class Customer(user):
    # membershipType = models.ForeignKey(MembershipType)
    colour = models.CharField(max_length=23)
