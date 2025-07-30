# 1. Calculate Square
def calculate_square(num):
    return num ** 2

# 2. Calculate Area of Rectangle
def area_of_rectangle(length, width):
    return length * width

# 3. Check Even or Odd
def is_even(num):
    return "Even" if num % 2 == 0 else "Odd"

# 4. Calculate Factorial
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# 5. Check Prime Number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# 6. Reverse a String
def reverse_string(s):
    return s[::-1]

# 7. Count Characters
def count_characters(s):
    return len(s)

# 8. Sum of Squares
def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

# 9. Check Palindrome
def is_palindrome(s):
    return s == s[::-1]

# 10. Calculate Fibonacci (first n numbers)
def fibonacci(n):
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# 11. Check Armstrong Number
def is_armstrong(num):
    order = len(str(num))
    return num == sum(int(digit) ** order for digit in str(num))

# 12. Check Leap Year
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
