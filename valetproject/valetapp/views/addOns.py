import six
from abc import ABCMeta


@six.add_metaclass(ABCMeta)
class Abstract_StatusOfValet(object):

    def getValetCost(self):
        pass


class Concrete_Valet(Abstract_StatusOfValet):

    def getValetCost(self):
        return 10



@six.add_metaclass(ABCMeta)
class Abstract_Valet_Decorator(Abstract_StatusOfValet):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def getValetCost(self):
        return self.decorated_valet.getValetCost()


class WaxCost(Abstract_Valet_Decorator):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def getValetCost(self):
        return self.decorated_valet.getValetCost() + 5


class PolishCost(Abstract_Valet_Decorator):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def getValetCost(self):
        return self.decorated_valet.getValetCost() + 12

class WashCost(Abstract_Valet_Decorator):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def getValetCost(self):
        return self.decorated_valet.getValetCost() + 3

class VacuumCost(Abstract_Valet_Decorator):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def getValetCost(self):
        return self.decorated_valet.getValetCost() + 4

class LeatherCost(Abstract_Valet_Decorator):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def getValetCost(self):
        return self.decorated_valet.getValetCost() + 6

class SteamCleanCost(Abstract_Valet_Decorator):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def getValetCost(self):
        return self.decorated_valet.getValetCost() + 4


