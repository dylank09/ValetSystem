from controllers.BaseController import BaseController
from controllers.UserController import UserController


class CustomerController(UserController):

    def __init__(self, model, view):
        super().__init__(model, view)

    def getMembershipType(self):
        name = self.model.getMembershipType()
        self.view.showMembershipType(str(name))
