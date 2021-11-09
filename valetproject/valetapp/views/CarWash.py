import six
from abc import ABCMeta

@six.add_metaclass(ABCMeta)
class Abstract_StatusOfValet(object):

   def getValetStatus(self):
      pass

   def getValetStatusEnd(self):
      pass

class Concrete_StatusOfValet(Abstract_StatusOfValet):

   def getValetStatus(self):
      return 'Wash has now started'

   def getValetStatusEnd(self):
      return 'Wash has now Finished'
   
