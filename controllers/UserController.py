from controllers.BaseController import BaseController


class UserController(BaseController):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def getFirstName(self):
        name = self.model.getFirstName()
        self.view.showFirstName(name)
