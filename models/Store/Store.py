from models.Store.StoreManager import StoreManager

class Store(object):

    
    """
    Constructor for Store class
    Store has the following data:
    name, location, GPSLocation, storeManager
    """
    def __init__(self, name, location, GPSLocation, storeManager, *args):
        super(Store, self).__init__(*args)
        self.name = name
        self.location = location
        self.GPSLocation = GPSLocation
        self.storeManager = storeManager
