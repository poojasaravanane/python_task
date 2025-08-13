# 1 single
class animal:
    def __init__(self,name):
       self.name=name
class dog(animal):
    def __init__ (self,name):
        super().__init__(name)
a=dog("robin")
print(a.name)

# 2 multiple    
class Pet:
    def __init__(self, owner):
        self.owner = owner
class Cat(animal, Pet):
    def __init__(self, name, owner):
        animal.__init__(self, name)
        Pet.__init__(self, owner)
cat = Cat("rambo", "anuja")
print(cat.name, cat.owner)

# 3 multilevel
class animal:
    def __init__(self,name):
        self.name=name
class cat:
    def __init__(self,name):
        super().__init__(name)
class kiten:
    def __init__(self,name):
        super().__init__(name)

a.kiten("buba")
print(a.name)


# 4 hierarchical
class Animal:
    def __init__(self, name):
        self.name = name

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)

cow = Cow("Ganga")
lion = Lion("Simba")
print(cow.name)  
print(lion.name)  

# 5 hybrid
class Animal:
    def __init__(self, name):
        self.name = name

class Pet:
    def __init__(self, owner):
        self.owner = owner

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

class Puppy(Dog, Pet): 
    def __init__(self, name, owner):
        Dog.__init__(self, name)
        Pet.__init__(self, owner)

puppy = Puppy("Bruno", "zoya")
print(puppy.name) 
print(puppy.owner)  
