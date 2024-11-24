class person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber

    def display(self):
        print("Name:", self.name)
        print("Id number:", self.idnumber)
class employee(person):
    def __init__(self, name, idnumber,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self, name, idnumber) #inheritance

obj=employee("Alex", 1388, 850000, "manager")
obj.display()