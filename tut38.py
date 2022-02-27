#multiple inheritence
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
class Programmer():
    leaves=60
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
        
    def printprog(self):
        return f"The programmer name is {self.name} salary is {self.salary} role is{self.role}"
class Coolprogrammer(Employee,Programmer):
    var=9
    language=["python","c++"]
    def printlanguage(self):
        print(self.language)
subham=Programmer("subham",600,"student")
karan=Coolprogrammer("Karan",800,"Engineer")
print(karan.printprog())
print(karan.printlanguage())