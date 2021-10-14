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
        self.rating = rating
        self.status = status
        self.valets = valets


    def setStoreName(self, name):
        self.name = name

    def showName(self):
        return self.name

    def showGPSLocation(self):
        return self.GPSLocation
    
    def showRating(self):
        return self.rating
    
    def showStatus(self):
        return self.status 