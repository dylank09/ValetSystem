from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

from .observer import Observer
from .membershiptype import MembershipType

    
class Customer(models.Model, Observer):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membershipType = models.ForeignKey(
        MembershipType, on_delete=models.RESTRICT, null=True)

    def update(self, subject):
        if subject.getPrice() > 0:

            if self.membershipType.colour == "gold":
                subject.setPrice(subject.getPrice()*0.7)
            elif self.membershipType.colour == "silver":
                subject.setPrice(subject.getPrice()*0.8)
            elif self.membershipType.colour == "bronze":
                subject.setPrice(subject.getPrice()*0.9)
