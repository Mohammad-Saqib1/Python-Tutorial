#single inheritence
class Employee:
    leaves=8
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    
    def printdetails(self):
        return f"The name is {self.name} , salary is {self.salary} and role is {self.role}"
    @classmethod
    def changes(cls,newleaves):
        cls.leaves=newleaves
        print(newleaves)
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("_")) 
class Programmer(Employee):
    leaves=60
    def __init__(self,aname,asalary,arole,language):
        self.name=aname
        self.salary=asalary
        self.role=arole
        self.language=language
    def printprog(self):
        return f"The programmer name is {self.salary} role is {self.role} salary is {self.salary} and language is {self.language}"

subham=Programmer("Subham",555,"programmer",["python","C++"])
harry=Employee("Harry",300,"Student")
print(harry.salary)
print(harry.printdetails())
harry.changes(34)
print(subham.printprog())
print(subham.leaves)