#abstraction:- make  small small part
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
harry=Employee("Harry",300,"Student")
print(harry.salary)
print(harry.printdetails())
harry.changes(34)