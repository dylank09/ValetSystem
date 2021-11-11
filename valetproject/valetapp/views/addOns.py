import six
from abc import ABCMeta


@six.add_metaclass(ABCMeta)
class Abstract_StatusOfValet(object):

    def getValetStatus(self):
        pass

    def getValetStatusEnd(self):
        pass


class Concrete_Valet(Abstract_StatusOfValet):

    def getValetStatus(self):
        return 'A new valet service type has started'

    def getValetStatusEnd(self):
        return 'The new valet service type has started'


@six.add_metaclass(ABCMeta)
class Abstract_Valet_Decorator(Abstract_StatusOfValet):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def getValetStatus(self):
        return self.decorated_valet.getValetStatus()

    def getValetStatusEnd(self):
        return self.decorated_valet.getValetStatusEnd()


class WaxStatus(Abstract_Valet_Decorator):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def getValetStatus(self):
        return self.decorated_valet.getValetStatus() + '\nWax has now started'

    def getValetStatusEnd(self):
        return 'Wax has now Ended \n' + self.decorated_valet.getValetStatusEnd()


class PolishStatus(Abstract_Valet_Decorator):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def getValetStatus(self):
        return self.decorated_valet.getValetStatus() + 'Polish has now started'

    def getValetStatus(self):
        return self.decorated_valet.getValetStatusEnd() + 'Polish has now Ended'
