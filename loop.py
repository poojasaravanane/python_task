##loop

##1
for i in range(1, 11):
    print(i)
##2
for i in range(1, 11):
    print("Square of" , i , "is",i ** 2)
##3
text = "character"
for char in text:
    print(char)
  
##4
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)
   
##5
elements = [10, 20, 30, 40]
for element in elements:
    print(element)

##6
for i in range(10,-1):
    print(i)
##7
for i in range(10, 21):
    if i % 2 == 0:
        print(i)
##8
for i in range(20, 51):
    if i % 5 == 0:
        print(i)     
##9
num = 8
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial of ",num," is ",fact)
      
##10
numbers = [5, 12, 3, 18, 7, 20]
for num in numbers:
    if num > 10:
        print(num)
##11
for num in range(10,21):
    if num > 10:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)  
##12
numbers = [10, 25, 5, 78, 3]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest number:", largest)
##13
text = "Hello World"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

##14
product = 1
for i in range(1, 6):
    product *= i
print("Product:", product)

##15
product = 1
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    product *= num
print("Product of numbers:", product)

##16
total = 0
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    total += num
print("Sum of numbers:", total)

