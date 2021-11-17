from abc import ABC,abstractmethod


class Item():
    @abstractmethod
    def accept(self):
        pass
