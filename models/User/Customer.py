from models.User.User import User

class Customer(User):
    def __init__(self, firstName, secondName, password, email, membershipType):
        super().__init__(firstName, secondName, password, email)
        self.membershipType = membershipType

    def getMembershipType(self):
        return self.membershipType.getDiscountPercentage()