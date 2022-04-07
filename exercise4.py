#print star

print("pattern printing")
num=int(input("enter num how many rows you print"))
bool_val=input("1 for true 0 for false")
if bool_val=="1":
    for i in range(0,num+1):
        print("*"*i)
if bool_val=="0":
    for i in range(num,0,-1):
        print("*"*i)