
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

#if you want to make same like contructor which takes a string instead of arguments in one line
    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))
    #if you want to dont take cls as form of arguments then use staticmethod
    @staticmethod
    def change_leaves(newleaves):
        print(newleaves)
    # @classmethod
    # def change_leaves(cls, newleaves):
    #     cls.no_of_leaves = newleaves
    #       print(newleaves)            

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")

# print(karan.role)
rohan.change_leaves(34)
# #
# print(harry.no_of_leaves)

