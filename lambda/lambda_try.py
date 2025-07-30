
add = lambda a, b: a + b

2. Find Maximum
maximum = lambda a, b: a if a > b else b

3. Square a Number
square = lambda x: x ** 2

4. Reverse a String
reverse = lambda s: s[::-1]

5. Check Even
is_even = lambda n: n % 2 == 0

Example usage
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", add(a, b))
print("Max:", maximum(a, b))
print("Square of first number:", square(a))

s = input("Enter a string: ")
print("Reversed string:", reverse(s))

n = int(input("Enter number to check even/odd: "))
print("Even" if is_even(n) else "Odd")

