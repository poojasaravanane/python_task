#1
def decorator1(func):
    def wrapper():
        print("get!!!")
        func()
        print("go!!!")
    return wrapper

@decorator1
def one():
    print("set!!!")
one()

#2
def decorator2(func):
    def wrapper(*args,**kwargs):
        print("this is apple")
        result=func(*args,**kwargs)
        print("this is cat")
        return result
    return wrapper
@decorator2
def two(name):
    print("this is",name)
two("mango")

# 3
class decorator3:
    @staticmethod
    def greet():
        print("this is static method")
decorator3.greet()

# 4
class decorator4:
    count = 0
    @classmethod
    def increase(cls):
        cls.count += 1
        print("Count is: ",cls.count)
decorator4.increase()
decorator4.increase()
decorator4.increase()

# 5
class Circle:
    def __init__(self, radius):
        self._radius = radius
    @property
    def area(self):
        return 3.14 * self._radius * self._radius
c = Circle(9)
print(c.area)  


