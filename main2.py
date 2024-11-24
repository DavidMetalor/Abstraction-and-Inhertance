class Person:
    def __init__(self,name,GPA):
        self.name=name
        self.GPA=GPA
    def display(self):
        print("NAME:", self.name)
        print("GPA:", self.GPA)
class Student(Person):
    def __init__(self, name, GPA, grade, ranking):
        self.grade=grade
        self.ranking=ranking
        super().__init__(name, GPA)
obj=Student("David", 3.86, 10, "1st")
obj.display()
    