# scope variables and global variables
"""
l=10
def func1(n):
    l=5
    m=10
    l=l+45
    print(l,m)
    print(n)
func1("This is a function")

n=10
def func2(r):


    global n
    n=n+90
    print(n)
    print(r)
func2("This is global accessing")
"""
x=89
def harry():
    x=20
    def rohan():
        global x
        x=88
        print(x)    
    rohan()
    print(x)
harry()
print(x)

        
    
    