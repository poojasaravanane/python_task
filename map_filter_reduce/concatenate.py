from functools import reduce
str1=input("enter a word:")
str2=input("enter a word:")
concatenate=reduce(lambda x,y:x+y,str2,str1)
print(concatenate)
