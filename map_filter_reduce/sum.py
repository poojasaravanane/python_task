from functools import reduce
numbers = [1,2,3,4,5,6,7,8,9]
square =map(lambda x:x**2,numbers)
square_number=reduce(lambda x,y:x+y,square)
print(square_number)  
