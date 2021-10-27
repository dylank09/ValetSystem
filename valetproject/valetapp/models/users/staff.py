from django.db import models
from .user import User


class Staff(User):
    # membershipType = models.ForeignKey(MembershipType)
    colour = models.CharField(max_length=23)
