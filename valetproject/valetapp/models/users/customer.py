from django.db import models
from django.contrib.auth.models import User
from ..item import Item

from .membershiptype import MembershipType
# from ..booking import Subject

# from .observer import Observer

# class Customer(models.Model, Observer):
    
class Customer(models.Model, Item):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membershipType = models.ForeignKey(
        MembershipType, on_delete=models.RESTRICT, null=True)

    def update(self, subject):
        if subject.getPrice() > 0:
            print("Customer Observer reacted to the event")

            if self.membershipType.colour == "gold":
                subject.setPrice(subject.getPrice()*0.7)
            elif self.membershipType.colour == "silver":
                subject.setPrice(subject.getPrice()*0.8)
            elif self.membershipType.colour == "bronze":
                subject.setPrice(subject.getPrice()*0.9)
    
    def getEmail(self):
        return self.user.email
    
    def accept(self, visitor):
        return visitor.visit(self)