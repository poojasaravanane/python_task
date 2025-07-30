##1 ADD()
set1={"orange","blueberry","graphes","strawberry"}
set1.add("drygraphes")
print(set1)

##2 CLEAR()
set2={"blue","black","orange"}
set2.clear()
print(set2)

##3 DIFFERENCE()
seta = {"mango", "graph", "orange"}
setb = {"pink", "orange", "yellow"}
setc = seta.difference(setb)
print(setc)

##4 DIFFERENCE_UPDATE()
a = {"mango", "graph", "orange"}
b = {"pink", "orange", "yellow"}
a-=b
print(a)

##5 COPY()
set2={"blue","black","orange"}
set2.copy()
print(set2)

##6 DISCARD()
set5={"orange","blueberry","graphes","strawberry"}
set5.discard("graphes")
print(set5)

##7 INTERSECTION()
x = {"mango", "graph", "orange"}
y = {"pink", "orange", "yellow"}
z=x&y
print(z)
##8 INTERSECTION_UPDATE()
x = {"mango", "graph", "orange"}
y = {"pink", "orange", "yellow"}
x&=y
print(x)
##9 ISDISJOINT()
seta = {"mango", "graph", "orange"}
setb = {"pink", "orange", "yellow"}
setc = seta.isdisjoint(setb)
print(setc)

##10 ISSUBSET()
set9={'d','e','f','g','h'}
set10={'a','b','c','d','e','f','g','h','i','j'}
set8=set9<=set10
print(set8)

##11 ISSUPERSET()
set10={'a','b','c','d','e','f','g','h','i','j'}
set9={'d','e','f','g','h'}
set8=set10>=set9
print(set8)

##12 POP()
set2={"blue","black","orange"}
set2.pop()
print(set2)

##13 REMOVE()
set5={"orange","blueberry","graphes","strawberry"}
set5.remove("graphes")
print(set5)

##14 SYMMETRIC_DIFFERENCE()
seta = {"mango", "graph", "orange"}
setb = {"pink", "orange", "yellow"}
setc = seta^setb
print(setc)

##15 SYMMETRIC_DIFFERENCE_UPDATE()
seta = {"mango", "graph", "orange"}
setb = {"pink", "orange", "yellow"}
seta^=setb
print(seta)

##16 UNION()
x = {"mango", "graph", "orange"}
y = {"pink", "orange", "yellow"}
x|y
print(x)

##17 UPDATE()
x = {"mango", "graph", "orange"}
y = {"pink", "orange", "yellow"}
x|=y
print(x)
