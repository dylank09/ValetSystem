class Store(object):

    """
    Constructor for Store class
    Store has the following data:
    name, location, GPSLocation, storeManager
    """

    def __init__(self, name, GPSLocation, storeManager, rating, status, valets):
        self.name = name
        self.GPSLocation = GPSLocation
        self.storeManager = storeManager

    def setStoreName(self, name):
        self.name = name

    def showName(self):
        return self.name
