from controllers.BaseController import BaseController


class CustomerController(BaseController):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def showName(self):
        name = self.model.showName()
        self.view.showName(name)
