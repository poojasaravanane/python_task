# method overloading
class Math:
    def add(self,a=0,b=0,c=0,d=0):
        print(a+b+c+d)

m = Math()
m.add(2,3)     
m.add(2,3,4)    
m.add(2,3,4,5)

# method overriding
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

Dog().speak() 
