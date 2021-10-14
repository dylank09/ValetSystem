class Membership(object):

    def __init__(self, colour, discountPercentage):
        self.colour = colour
        self.discountPercentage = discountPercentage

    def getDiscountPercentage(self):
        return self.discountPercentage