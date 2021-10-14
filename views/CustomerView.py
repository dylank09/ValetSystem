from views.UserView import UserView


class CustomerView(UserView):
    def __init__(self):
        print("")

    def showMembershipType(self, membershipType):
        print("This person has a  " + membershipType + " percentage discount")
