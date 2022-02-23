
class Employee:
    no_of_leaves = 8
#this is constructor if you want to do work with object contructor handle them
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    
    #if you want to access to change in class by instance varibles then makes classmethod
    @classmethod

    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
        print(newleaves)
harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Harry", 255, "Instructor")
print(harry.salary)
rohan.change_leaves(34)
rohan.change_leaves(40)

