#operator overloading and dunder method
class Employee:
    leaves=8
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"The name is{self.name},salary is {self.salary}and role is{self.role}"
    @classmethod
    def change_leaves(self,newleaves):
        self.leaves=newleaves
        return newleaves
    def __add__(self,other):
        return f"The salary is {self.salary+other.salary}and name is {self.name+other.name}"
    def __repr__(self):
        return f"Employee {self.name}, {self.salary},{self.role}"
    def __str__(self):
        return f"The name is {self.name} ,{self.salary} and {self.role}"
    def __truediv__(self,other):
        return self.salary/other.salary
emp1=Employee("Harry",400,"Coder")
emp2=Employee("Rohan",600,"Business Man")
print(emp1.change_leaves(34))
#if you want to apply add or any function at class object then use dunder function
# print(emp1+emp2)
#dunder function:-It is special types of function
print(emp1+emp2)
#if you want to print all object's value then make it __repr__ and __str__
print(repr(emp1))
print(str(emp2))
print(emp1/emp2)

