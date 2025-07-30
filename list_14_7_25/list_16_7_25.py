##1
list1=[1,2,3,4,5,6,7,8,9]
list1.reverse()
print(list1)

##2
list2=[1,-4,3,-5,6,8,-7,2]
positive=0
negative=0
for i in list2:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1

print("count of positive numbers are ",positive)
print("count of negative numbers are ",negative)
##3
list3=[3,5,6,8,9,12,18,16]
for i in list3:
    if i%3==0:
        print("numbers divisible by 3 is ",i)
##4
list4=[1,3,4,5,6,7,5,9,4,5,6,3]
x=list4.count(5)
print(x)

##5
numbers = [0,1,2,0,3,0,4,5,0]
x = []
for num in numbers:
    if num != 0:
        x.append(num)
print(x)  
##6
numbers = [4,-2,7,-5,0,3,-1]
for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0
print(numbers)  

##7
list7=[2,3,4,5,6,7,8,9]
square=[i*i for i in list7]
print(square)
##8
numbers = [1, 2, 3, 2, 5, 1, 6, 7, 3, 5]
duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
print("Duplicate numbers in list are ",duplicates)

##10
numbers = [3, 12, 5, 8, 15, 9, 20]
for num in numbers:
    if num < 10:
        print( num) 

