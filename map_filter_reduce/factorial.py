from functools import reduce
num=[1,2,3,4,5,6,7,8,9]
factorial=reduce(lambda x,y:x*y,num )
print(factorial)
