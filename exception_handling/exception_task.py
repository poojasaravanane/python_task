#1
# try:
#     num1=int(input("enter the number:"))
#     num2=int(input("enter the number:"))
#     total=num1/num2
#     print(total)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("enter correct value")


#2
# try:
#     x = input("Enter a number: ")
#     number = int(x)
#     print("You entered:", number)
# except ValueError:
#     print("Invalid input")

# 3
# a = {
#     "name": "Pooja",
#     "age": 21,
#     "course": "BCA",
#     "city": "puducherry"
# }
# try:
#     key = input("Enter any key: ")
#     value = a[key]
#     print("Value:", value)
# except KeyError:
#     print("Key not found in the dictionary.")

# 4
# try:
#     num = int(input("Enter an even number: "))
#     if num % 2!= 0:
#         raise ValueError("The number is not even.")
#     print("You entered an even number:", num)
# except ValueError as e:
#     print("Error:", e)

# 5
# try:
#     age = int(input("Enter your age: "))
#     if age < 0:
#         raise ValueError("Age cannot be negative")
#     print("Your age is ", age)
# except ValueError as e:
#     print("Error:", e)

# 6
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    n = input("Enter an operation (+, -, *, /): ")
    if n == "+":
        total=num1 + num2
    elif n == "-":
        total = num1 - num2
    elif n == "*":
        total = num1 * num2
    elif n =="/":
        if num2 == 0:
            raise ZeroDivisionError("cant't divide by zero")
        total=num1/num2
    else:
        raise ValueError("invalid")
    print(total)
except ValueError as ve:
    print(ve)
except ZeroDivisionError as ze:
    print(ze)
