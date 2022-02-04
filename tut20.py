# lambda function, it is one liner function
def add(a,b):
#     c=a+b
#     print(c)
# add(4,6)
#If yoc can want to return any value then you can always print function example given below
    return a+b
print(add(4,6))
#use lambda function
add=lambda x,y:x+y
print(add(6,12))



g=[[1,4],[8,5],[6,8],[2,9]]
g.sort(key=lambda x:x[0])
print(g)

g=[[1,8],[8,3],[6,2],[2,1]]
g.sort(key=lambda x:x[1])
print(g)
#False contains assending order
g=[[1,8],[8,3],[6,2],[2,1]]
g.sort(reverse=False)
print(g)
#True contains decending order
g=[[1,8],[8,3],[6,2],[2,1]]
g.sort(reverse=True)
print(g)