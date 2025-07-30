numbers = [7,3,4,5,0,6,3]
product = 1
for num in numbers:
    if num == 0:
        continue  
    product *= num  
print("Product of number:", product)
