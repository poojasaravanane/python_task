#8 filter out the numbers grater than 10 in a list
number=[1,67,4,5,12,82,15,7,91]
greater=list(filter(lambda x: x > 10,number))
print(greater)
