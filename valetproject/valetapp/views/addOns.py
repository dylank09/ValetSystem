import six 
from abc import ABCMeta
from views.CarWash import Abstract_Valet

@six.add_metaclass(ABCMeta)
class Abstract_Valet_Decorator(Abstract_Valet):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def get_cost(self):
        return self.decorated_valet.get_cost()

    def get_duration(self):
        return self.decorated_valet.get_duration()

class Wax(Abstract_Valet_Decorator):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def get_cost(self):
        return self.decorated_valet.get_cost() + 5

    def get_duration(self):
        return self.decorated_valet.get_duration() + 1

class Polish(Abstract_Valet_Decorator):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def get_cost(self):
        return self.decorated_valet.get_cost() + 10

    def get_duration(self):
        return self.decorated_valet.get_duration() + 1