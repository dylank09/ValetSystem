from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
import uuid


class Staff(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    staffId = models.UUIDField(
        max_length=100, blank=True, unique=True, default=uuid.uuid4)

    def getStaffEmail(self):
        return self.user.email

    def accept(self, visitor):
        return visitor.visit(self)
        