#map(),filter(),reduce()
############# MAP ##########
numbers=["34","50","45"]
for i in range(len(numbers)):
    numbers[i]=int(numbers[i])
numbers[2]=numbers[2]+1
print(numbers[2])
#Easy done by use of map()
numbers=list(map(int,numbers))
numbers[1]=numbers[1]+1
print(numbers[1])
def sq(a):
    return a*a
b=sq(3)
print(b)
#for multiple value
num=[1,2,3,4,5,6]
square=list(map(sq,num))
print(square)
#in one line
square=list(map(lambda x:x*x,num))
print(square)


############ FILTER ########

list_1=[1,2,3,4,5,6,7,8,9]
def greater_than_5(num):
    return num>5
c=list(filter(greater_than_5,list_1))
print(c)
#done in easy way
c=list(filter(lambda x:x>5,list_1))
print(c)

############ REDUCE #########
from functools import reduce
list_2=[1,2,3,4,5,2,1,2]
num1=1
for i in list_2:
    num1=num1*i
print(num1)
#done in easy way
num1=reduce(lambda x,y:x*y,list_2)
print(num1)
