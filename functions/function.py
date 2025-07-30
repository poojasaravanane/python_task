##1 
def square(num):
    return num ** 2
x=square(5)
print("square is ",x)

##2
def rectangle(length, width):
    return length * width
x=rectangle(3,5)
print("area of rectangle is ",x)

##3
def check_even_odd(num):
    if num % 2 == 0:
        print("It is Even:", num)
    else:
        print("It is Odd:", num)
n = int(input("Enter the number: "))
check_even_odd(n)

##4
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter the number: "))
if num < 0:
    print("No factorial for negative numbers.")
else:
    print("The factorial is:", factorial(num))

##5
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

##6
def reverse(s):
    return s[::-1]
text = input("Enter a string: ")
print("Reversed string:", reverse(text))

##7
def count(s):
    return len(s)
text = input("Enter characters: ")
print("the count of characters are ", count(text))

##8
def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))
num = int(input("Enter a number: "))
print("Sum of squares from 1 to", num, "is:", sum_of_squares(num))

