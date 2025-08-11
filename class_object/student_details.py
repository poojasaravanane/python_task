## std
class std:
    name = "aaa"
    age = 18
    id = 1012
    city = "pondy"

    def dept(self,dept):
        print(f"The student {self.name} is {dept} department. ")

std1=std()
std1.name="pooja"
print("name:",std1.name)
std1.age=19
print("age:",std1.age)
print("id:",std1.id)
std1.dept("BCA")

std2=std()
std2.name="anu"
print("name:",std2.name)
std2.age=18
print("age:",std2.age)
std2.id=1013
std2.city="chennai"
print("id:",std2.id)
print("city:",std2.city)
std2.dept("Bcs.CS")

std3=std()
std3.name="nandhu"
std3.id=1016
std3.city="lavasa"
print("name",std3.name)
print("id",std3.id)
print("city",std3.city)
std3.dept("Bsc.DS")