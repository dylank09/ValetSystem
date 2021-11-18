from django.db import models


class MembershipType(models.Model):
    colour = models.CharField(max_length=15)

    def getColour(self):
        return self.colour

    def accept(self, visitor):
        return visitor.visit(self)
