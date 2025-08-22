from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):   
        return self.side * self.side

    def perimeter(self):  
        return 4 * self.side
    
class rectangle(shape):
    def __init__(self,side):
        self.side =side  

square = Square(5)

print("Square: Area =", square.area(), ", Perimeter =", square.perimeter())
