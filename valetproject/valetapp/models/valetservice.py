from django.db import models
from abc import ABCMeta, abstractmethod

class Valet(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def getName(self):
        return self.name


class BaseValet(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def addDuration():
        """add duration"""


class CompositeBaseValet(BaseValet):
    def __init__(self):
        self.childValet = []
        self.cost = 0
        self.duration = 0

    def add(self, valet):
        self.childValet.append(valet)

    def addDuration(self):
        for g in self.childValet:
            for h in g.childValet:
                self.duration += h.addDuration()
        print(self.duration)
        return self.duration


class CompositeExterior(CompositeBaseValet):
    def __init__(self):
        self.childValet = []
        self.cost = 0
        self.duration = 0

    def add(self, valet):
        self.childValet.append(valet)

    def addDuration(self):
        for g in self.childValet:
            self.duration += g.addDuration()
        print(self.duration)


class Wash(CompositeExterior):
    def addDuration(self):
        return 5


class Wax(CompositeExterior):
    def addDuration(self):
        return 10


class Polish(CompositeExterior):
    def addDuration(self):
        return 12


class CompositeInterior(CompositeBaseValet):
    def __init__(self):
        self.childValet = []
        self.cost = 0
        self.duration = 0

    def add(self, valet):
        self.childValet.append(valet)

    def addDuration(self):
        for g in self.childValet:
            self.duration += g.addDuration()
        print(self.duration)


class Hoover(CompositeInterior):
    def addDuration(self):
        return 10


class SteamClean(CompositeInterior):
    def addDuration(self):
        return 4


class Leather(CompositeExterior):
    def addDuration(self):
        return 5
