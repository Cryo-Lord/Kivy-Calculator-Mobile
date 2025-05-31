#clase calculadora para encapsular los calculos correspondientes
from abc import ABC, abstractmethod 

class Calculator(ABC):
    
    @abstractmethod
    def calculate():
        pass

    @abstractmethod
    def save():
        pass

    @abstractmethod
    def recall():
        pass

class Mathematics(Calculator):

    def calculate(abstractClass, input):
        #calculate result with the operation given
        print(abstractClass)
        print(input)
        try:
            return str(eval(input))
        except:
            return "Error"

    def save(memory:list): 
        #save into database
        pass

    def recall():
        pass

class Averager(Calculator):
    memory = []

    def save(result:float):
        #save into database
        memory.append(result)

    def calculate(input:list[dict]):
        #calculate grade with the data received
        total = 0
        for data in input:
            total += data.grade*data.percentage
        self.save(total)
        return total

    def recall():
        #recall last result
        pass

class Scientific(Calculator):
    pass
