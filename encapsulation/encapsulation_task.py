class student:
    def __init__(self,name,mark,grade):
        self.name=name
        self._mark=mark
        self.__grade=grade
    def display(self):
        print("name: ",self.name)
        print("mark: ",self._mark)
        print("grade: ",self.__grade)
    
std1=student("anu",89,"B")
std2=student("diya",96,"A")
std3=student("zoya",76,"C")
std4=student("bob",56,"E")

print(std1.name)
print(std1._mark)
print(std1._student__grade)

print(std2.name)
print(std2._mark)
print(std2._student__grade)

print(std3.name)
print(std3._mark)
print(std3._student__grade)

print(std4.name)
print(std4._mark)
print(std4._student__grade)