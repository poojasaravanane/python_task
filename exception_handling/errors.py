# 1 arithmetic error
try:
    x=9/0
except ArithmeticError:
    print("its zero division error")
except:
    print("something wrong")

# 2 attribute error
x=50
try:
    x.append(6)
except AttributeError:
    print("its can't append")
except:
    print("something wrong")

# 3 import error
from os import math

# 4 indentation error
if 5>2:
print("correct the indentation error")

# 5 index error
x=['a','b','c']
try:
    print(x[4])
except IndexError:
    print("something wrong with indexing")

# 6 keyerror
a = {
    "name": "Pooja",
    "age": 21,
    "course": "BCA",
    "city": "puducherry"
}
try:
    key = input("enter the key: ")
    value = a[key]
    print("Value:", value)
except KeyError:
    print("Key not found in the dictionary.")

# 7 name error
try:
    print(pooja)
except NameError:
    print("its a name error")

# 8 overflow error
import math as m
print(m.exp(1090))

# 9 syntax error
if 5>2
       print("something wrong")

# 10 runtime error
def a():
    raise RuntimeError("Something went wrong!")
a()

# 11 type error
try:
    x="a"+ 10
except TypeError:
    print("its a type error")

# 12 value error
x= int("hiii")
print(x)

# 13 zero division error
x=4/0
print(x)