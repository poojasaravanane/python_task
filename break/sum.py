sum = 1 
while True:
    num = int(input("Enter a number: "))
    if num > 0:
        continue
    if num < 0:
        print("stop")
        break  
    sum + num  
    print(num)
print("sum of numbers is:", sum)
