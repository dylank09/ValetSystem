from django.db import models
from abc import ABCMeta, abstractmethod


class BaseValet(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def addCost():
        """add cost"""
    def addDuration():
        """add duration"""


class CompositeBaseValet(BaseValet):
    def __init__(self):
        self.childValet = []
        self.cost = 0
        self.duration = 0

    def add(self, valet):
        self.childValet.append(valet)

    def addCost(self):
        for g in self.childValet:
            for h in g.childValet:
                self.cost += h.addCost()
        print(self.cost)

    def addDuration(self):
        for g in self.childValet:
            for h in g.childValet:
                self.duration += g.addDuration()
        print(self.duration)


class CompositeExterior(CompositeBaseValet):
    def __init__(self):
        self.childValet = []
        self.cost = 0
        self.duration = 0

    def add(self, valet):
        self.childValet.append(valet)

    def addCost(self):
        for g in self.childValet:
            self.cost += g.addCost()
        print(self.cost)

    def addDuration(self):
        for g in self.childValet:
            self.duration += g.addDuration()
        print(self.duration)


class Wash(CompositeExterior):
    def addCost(self):
        return 2

    def addDuration(self):
        return 5


class Wax(CompositeExterior):
    def addCost(self):
        return 4

    def addDuration(self):
        return 10


class Polish(CompositeExterior):
    def addCost(self):
        return 5

    def addDuration(self):
        return 12


class CompositeInterior(CompositeBaseValet):
    def __init__(self):
        self.childValet = []
        self.cost = 0
        self.duration = 0

    def add(self, valet):
        self.childValet.append(valet)

    def addCost(self):
        for g in self.childValet:
            self.cost += g.addCost()
        print(self.cost)

    def addDuration(self):
        for g in self.childValet:
            self.duration += g.addDuration()
        print(self.duration)


class Hoover(CompositeInterior):
    def addCost(self):
        return 2

    def addDuration(self):
        return 10


class SteamClean(CompositeInterior):
    def addCost(self):
        return 15

    def addDuration(self):
        return 4


class Leather(CompositeExterior):
    def addCost(self):
        return 10

    def addDuration(self):
        return 5
