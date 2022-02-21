#instance and class variables you can make variables inside the class and outside also
class Employee:
    no_of_leaves=8
    

harry=Employee()
rohan=Employee()
harry.name="Harry"
harry.salary=20000
harry.role="Instructer"
rohan.name="Rohan"
rohan.salary=20000
rohan.role="Model"
print(harry.salary)
print(rohan.role)
print(rohan.no_of_leaves)
Employee.no_of_leaves=10
print(Employee.__dict__)

print(rohan.no_of_leaves)
print(Employee.__dict__)


