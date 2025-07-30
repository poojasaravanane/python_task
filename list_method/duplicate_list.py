numbers4 = [1, 2, 3, 2, 5, 1, 6, 7, 3, 5]
duplicates = []

for num in numbers4:
    if numbers4.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
print("Duplicate elements in the array:",duplicates)
