#F-string
import math
me="Harry"
a1=3
a="This is %s %s "%(me,a1)
print(a)
a="This is {1} {0}"
b=a.format(me,a1)
print(b)


#F-string
#print any datatype more and more times
c=f"This is {me} {a1} {math.cos(120)}"
print(c)
