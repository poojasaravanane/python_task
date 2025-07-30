## operators
b="anu"
a=1
c=True
d=4.0
e=6
f=4
x=2
y=3
##arithmatics
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)

## assignment
x==4
print(x)
x+=6
print(x)
y-=7
print(y)
y*=8
print(y)
e/=5
print(e)
f%=4
print(f)
x//=5
print(x)
y**=5
print(y)
x&=5
print(x)
f>>=5
print(f)
f<<=5
print(f)
print(x:=5)

## comparison operator
print(e==f)
print(e!=f)
print(e>f)
print(e<f)
print(e>=f)
print(e<=f)


##logical operator

w=5
##AND
print(w>3 and w<7)
##OR
print(w>9 or w<3)
##NOT
print (not(w>4 and w<7))



##identity operator
g=["ant","butterfly"]
h=["ant","butterfly"]
j=g
##IS
print(j is g)
print(g is h)
##IS NOT
print(g is not h)
print(g == h)


##membership operator
insects=["ant","butterfly"]

print("ant" in insects)
print("bees" in insects)
print("butterfly" not in insects)


##bitwise operator
##AND
z=10
m=3
print(z&m)
print(20&2)
print(z|m)
print(10|5)
print(z^m)
print(30^7)
print(~4)
print(20>>5)
print(40<<5)
