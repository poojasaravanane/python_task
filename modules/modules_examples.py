#add
def add(a,b):
    return a+b
#subtract
def sub(a,b):
    return a-b
#multiple
def multiple(a,b):
    return a*b
#divide
def divide(a,b):
    return a/b

#dictionary
diction = {
    "name": "anu",
    "dept": "mba",
    "salary": 10000
}
def get_name():
    return diction["name"]

def get_dept():
    return diction["dept"]

def get_salary():
    return diction["salary"]  

#area of shapes
import math
def area_circle(radius):
    return math.pi * radius ** 2

def area_square(side):
    return math.side**2

def area_rectangle(length,width):
    return math.length*width

def area_triangle(base,height):
    return 1/2 * base*height