#Daimond shape problem in multiple inheritance
#if you want to access multiple inheritance then use it
class A:
    def met(self):
        print("This is a method from class A")
class B:
    pass
    # def met(self):
    #     print("This is a method fromclass B")
class C(A):
    pass
    # def met(self):
    #     print("This is a method from class C")
class D(C,B):
    pass
    # def met(self):
        
        # print("This is a method from class D")
        # print("This is shape problem in class D")
        

a=A()
b=B()
c=C()
d=D()
d.met()