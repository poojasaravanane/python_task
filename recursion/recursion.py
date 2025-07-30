def recursion_one(i):
    if(i > 0):
        x= i + recursion_one(i - 1)
        print(x)
    else:
      x= 0
    return x
print("print from 1 to 10")
recursion_one(10)
