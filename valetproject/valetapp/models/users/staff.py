from django.db import models


class Staff(models.Model):
    # membershipType = models.ForeignKey(MembershipType)
    colour = models.CharField(max_length=23)
