##1 add two numbers
x=lambda a,b:a+b
print(x(10,26))

##2 find the maximum of two numbers
maximum = lambda a, b: a if a > b else b
a=15
b=61
print("Max:", maximum(a, b))

##3 square numbers
square = lambda x: x ** 2
x = int(input("Enter any number: "))
print("Square of the number: ", square(x))

##4 reverse string
reverse = lambda s: s[::-1]
s=input("enter any string: ")
print("The reversed string is ",reverse(s))

##5 check if a number is even
even = lambda n: n % 2 == 0
n=int(input("enter any number: "))
print("the given number is even" if even(n) else "the given number is odd")

