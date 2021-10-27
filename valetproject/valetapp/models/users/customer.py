from django.db import models
from .membershiptype import MembershipType
from .user import User


class Customer(User):
    firstname = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")
    membershipType = models.ForeignKey(MembershipType, on_delete=models.RESTRICT, null=True)
    colour = models.CharField(max_length=23, null=True)
