class User(object):

    def __init__(self, firstName, surname, password, email):
        self.firstName = firstName
        self.surname = surname
        self.password = password
        self.email = email

    def getFirstName(self):
        return self.firstName
    
    def setFirstName(self, name):
        self.name = name

    def getSurname(self):
        return self.surname

    def setSurname(self, surname):
        self.surname = surname

    def setPassword(self, password):
        self.password = password

    def setEmail(self, email):
        self.email = email

    def getEmail(email):
        return email
    