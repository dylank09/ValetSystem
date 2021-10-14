class Valet(object):
    
    """
    Constructor for Store class
    Store has the following data:
    name, location, GPSLocation, storeManager
    """

    def __init__(self, type, price):
        self.type = type
        self.price = price
        

    def setType(self, name):
        self.name = name

    def getType(self):
        return self.name
