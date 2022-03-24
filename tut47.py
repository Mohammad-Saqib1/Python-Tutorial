#Generators
#if you want to iteration one by one then use generators
def gen(n):
    for i in range(n):
        yield i
        #yield only use for int by function
g=gen(3)
# print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
for i in g:
    print(i)
h="Harry"
#if you want to iteration of string use __iter__() 

ier=iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# for c in h:
#     print(c)
