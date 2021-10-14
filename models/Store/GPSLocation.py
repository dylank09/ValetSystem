class GPSLocation(object):

    """
    Constructor for GPSLocation class
    Store has the following data:
    Xcord, Ycord
    """

    def __init__(self, Xcord, Ycord):
        self.Xcord = Xcord
        self.Ycord = Ycord 


    def setXcord(self, Xcord):
        self.Xcord = Xcord

    def showYcord(self, Ycord):
        return self.Ycord
