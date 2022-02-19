#decorators
def dec1(func1):
    def nowexe():
        print("Executing now")
        func1()
        print("Executed")
    return nowexe
@dec1
def who_is_harry():
    print("Harry is a good boy")
who_is_harry()