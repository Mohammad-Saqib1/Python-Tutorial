#overriding and super()
class A:
    classvar1="I am a class variable in class A"
    def __init__(self):
        self.var1="I am inside class A's constructor"
        self.classvar1="Instance var in class A"
        self.special="special"
class B(A):
    #overriding class A
    classvar1="I am in class B"
    def __init__(self):
        self.var1="I am inside class B's contructor"
        self.classvar1="Instance var in class B"
        #if you want to access any variable of class A after overridind then you can make a super()in class B that means explitly define
        super().__init__()
a=A()
b=B()
# print(b.special,b.var1,b.classvar1)
# print(b.special)
print(b.classvar1)
print(a.classvar1)
