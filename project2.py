#If you want to distrube apple in our student
try:
    apples=int(input("Enter the number of apples"))
    mx=int(input("Enter the upper bond"))
    mn=int(input("Enter the lower bond"))
    for i in range(mn,mx+1):
        if apples%i==0:
            print(f"{i} is a divisor {apples}")
        else:
            print(f"{i} is not a divisor {apples}")
except Exception as e:
    print(e,"wrong input! please enter int value")
