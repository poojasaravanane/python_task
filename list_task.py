##1
numbers=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for x in numbers:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print("even_numbers",even)
print("odd_numbers",odd)
even.extend(odd)
print(even)

##2
numbers
    
