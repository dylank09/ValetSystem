from django.db import models
from .membershiptype import MembershipType
from .user import User


class Customer(User):
    membershipType = models.ForeignKey(
        MembershipType, on_delete=models.RESTRICT, null=True)
