from django.db import models

class MembershipType(models.Model):
    colour = models.CharField(max_length=15)
    # discount = models.DecimalField(max_digits=20, decimal_places=2)

    def getColour(self):
        return self.colour

    def accept(self, visitor):
        return visitor.visit(self)