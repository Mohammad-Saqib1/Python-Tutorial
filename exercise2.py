#Faulty calculator
print("Enter first number")
n1=int(input())
print("Enter second number")
n2=int(input())
print("Enter any operation,+ - * /")
n3=input()
if n1==45 and n2==3 and n3=='*':
    print("777")
elif n1==56 and n2==9 and n3=='+':

    print("77")
elif n1==56 and n2==6 and n3=='/':
    print("4")
else:
    if n3=='*':
        print(n1*n2)
    elif n3=='+':
    
        print(n1+n2)
    elif n3=='-':
        print(n1-n2)
    else:
        print(n1/n2)
