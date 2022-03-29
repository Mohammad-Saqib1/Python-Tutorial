# #Else and finally in try except
# f=open("does.txt")
#except and else only one run at a time
try:
    f1=open("harry.txt")
    a=f1.read()
    print(a)
    
except Exception as e:
    print(e,"This is an important file")
else:
    print("This will run only if except is not running")
finally:
    print("Run this anyway")
f1.close()



















