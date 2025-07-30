product = 1 
while True:
    num = int(input("Enter a number: "))
    
    if num < 0:
        continue
    
    if num == 0:
        print("stop")
        break  
    
    product *= num  
    
    print(num)

print("Product of numbers is:", product)


