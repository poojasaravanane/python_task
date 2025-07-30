def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])
numbers = [1,2,3,4,5,6,7,8,9,10]
print("the sum of list:",sum_list(numbers))
