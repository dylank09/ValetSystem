import six 
from abc import ABCMeta
from views.CarWash import Abstract_Valet

@six.add_metaclass(ABCMeta)
class Abstract_Valet_Decorator(Abstract_Valet):

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
        return self.decorated_valet.getValetStatus() + 'Wax has now started'

    def getValetStatus(self):
        return self.decorated_valet.getValetStatusEnd() + 'Wax has now Ended'

class PolishStatus(Abstract_Valet_Decorator):

    def __init__(self, decorated_valet):
        self.decorated_valet = decorated_valet

    def getValetStatus(self):
        return self.decorated_valet.getValetStatus() + 'Polish has now started'

    def getValetStatus(self):
        return self.decorated_valet.getValetStatusEnd() + 'Polish has now Ended'

    