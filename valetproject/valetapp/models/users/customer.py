from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from abc import ABC, abstractmethod

from .membershiptype import MembershipType
from ..booking import Subject

class Observer(ABC):

    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

class Customer(models.Model, Observer):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membershipType = models.ForeignKey(
        MembershipType, on_delete=models.RESTRICT, null=True)

    def update(self, subject: Subject) -> None:
        if subject.getPrice() > 0:
            print("Customer Observer reacted to the event")

            if self.membershipType.colour == "gold":
                subject.setPrice(subject.getPrice()*0.7)
            elif self.membershipType.colour == "silver":
                subject.setPrice(subject.getPrice()*0.8)
            elif self.membershipType.colour == "bronze":
                subject.setPrice(subject.getPrice()*0.9)
