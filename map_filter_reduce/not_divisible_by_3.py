#filer the list not divisible by 3
numbers = [1, 3, 5, 6, 9, 10, 12, 14, 15]
divisible_by_3 = list(filter(lambda x: x % 3 != 0, numbers))
print(divisible_by_3) 
