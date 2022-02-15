#how import works
#never makes module in module name
import file2
print(file2.a)
file2.printjoke("\nThis is file 2")
# import sys
# print(sys.path)
#If you want to access a of file2 directly ,then you write
from file2 import a
print(a)
