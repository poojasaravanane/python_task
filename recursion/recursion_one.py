def recursion_one(i):
    if i > 0:
        x = i + recursion_one(i - 1)
        return x
    else:
        return 0

def reverse(i):
    if i > 0:
        x = recursion_one(i)
        print(x)
        reverse(i - 1)

print("print from 10 to 1")
reverse(10)


