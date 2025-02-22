#clase calculadora para encapsular los calculos correspondientes
from abc import ABC, abstractmethod, property

class calculator(ABC):
    @property
    memory = []

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
    memory = []

    def calculate(input:str):->float
        try:
            return eval(input)
        except Error as e:
            return f"Error: {e}"

class averager(calculator):
    memory = []

    def save(result:float):-> None
        memory.append(result)

    def calculate(input:list[dict]):
        total = None
        for data in input:
            total += data.grade*data.percentage
        self.save(total)
        return total

class cientific(calculator):
    pass
