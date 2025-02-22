#clase calculadora para encapsular los calculos correspondientes
from abc import ABC, abstractmethod, property

class calculator(ABC):
    @property
    memory = []

    @abstractmethod
    def input():
        pass

    @abstractmethod
    def calculate():
        pass

    @abstractmethod
    def save():
        pass

    @abstractmethod
    def recall():
        pass

class mathematics(calculator):
    self.super(__init__)


class averager(calculator):
    pass

class cientific(calculator):
    pass
