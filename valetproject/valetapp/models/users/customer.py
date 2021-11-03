from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .membershiptype import MembershipType


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membershipType = models.ForeignKey(
        MembershipType, on_delete=models.RESTRICT, null=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
    instance.customer.save()
