#function and docstring
a=9
b=8
c=sum((a,b))
print(c)
def function1():
    """
    This is function is not use for 3 variables
    """
    print("You are in function 1")
function1()
def function2(c,d):
    print(c+d)
function2(4,6)
def function3(e,f):

    """
    This is only for calculate avg

    """
    avg=(e+f)/2
    print(avg)
function3(6,8)

def func(g,h):

    """
    use for moretimes
    """
    sub=g-h
   # print(sub)
    return sub
v=func(10,3)
print(v)
j=v+3
print(j)
print(func.__doc__)
print(function1.__doc__)

    
    