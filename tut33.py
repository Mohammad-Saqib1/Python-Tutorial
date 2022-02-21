

class Employee:
    no_of_leaves = 8
#this is constructor if you want to do work with object contructor handle them
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


harry = Employee("Harry", 255, "Instructor")

# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"

# rohan = Employee()
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

# print(rohan.printdetails())
print(harry.salary)

