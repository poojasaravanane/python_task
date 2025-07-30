##1 create a list of 5 integers and print the second and fourth elements.
num=[1,2,3,4,5]
print("second element: ",num[1])
print("fourth element: ",num[3])


##2 append a new element to a list and then insert another at the begining.
colour=["blue","black","yellow"]
colour.append("pink")
colour.insert(0,"purple")
print(colour)

##3 remove the last element of a list using a suitable method.

place=["pondy","coorg","kochi"]
place.pop()
print(place)

##4 check whether a specific item exists in the list and print a message.
nums=[2,5,7,9,4,8,0,1]
if 4 in nums:
    print("yes, it has 4 in nums")
else:
    print("No, it does not has 4 in nums")

##5 loop through a list and print only the elements that are even numbers.
numbers=[2,4,5,7,6,9]
for n in numbers:
    if n%2==0:
        print(n)

##6 sort a list od=f numbers in descending order.
elements=[1,2,3,4,5,6,7,8,9]
elements.sort(reverse=True)
print(elements)

##7 combine two list into a single list.
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list1.extend(list2)
print(list1)

##8 find and print the largest and smallest number in a list.
element=[34,76,54,29,79]
print("largest number is ",max(element))
print("smallest number is ",min(element))

##9 count how many times a specific value occurs in a list.
list3=[3,5,4,2,5,6,7,5,8,6,9,5]
x=list3.count(5)
print(x)

##10 use list comprehension to create a new list with the square of each number from an existing list.
list4=[2,3,4]
square=[i*i for i in list4]
print(square)


