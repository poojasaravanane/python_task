##nested looping
rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
## 1   
for i in range(1,6,+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()

##2
for i in range(1,6,+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()   
##3
for i in range(1, 6):
    for j in range(65, 65+i):
        print(chr(j), end=" ")
    print()

##4
for i in range(1, 6):
    char = chr(64+i)
    for j in range(i):
        print(char, end=" ")
    print()
##5
rows=5    
for i in range(rows,0,-1):
    for j in range(i):
        print("*",end=" ")  
    print()
##6
for i in range(5,0,-1):
    for j in range(i):
        print(i,end=' ')
    print()
##7
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
##8
for i in range(5,0,-1):
    for j in range(65, 65+i):
        print(chr(j), end=" ")
    print()
##9
for i in range(5, 0,-1):
    ch = chr(64+i)
    for j in range(i):
        print(ch, end=" ")
    print()

##10
num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
##11
##12
##13
##14
