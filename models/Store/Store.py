class Store(object):

    """
    Constructor for Store class
    Store has the following data:
    name, location, GPSLocation, storeManager
    """

    def __init__(self, name):
        self.name = name
        # self.location = location
        # self.GPSLocation = GPSLocation
        # self.storeManager = storeManager

    def setStoreName(self, name):
        self.name = name

    def showName(self):
        return self.name
