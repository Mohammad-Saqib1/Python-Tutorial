#break and continue
i=0
while (True):
    if i+1<5:
        i=i+1
        continue
    print(i+1,end=" ")
    if (i==44):
        break
    i=i+1
#quiz
while(True):
    inp=int(input("Enter a number\n"))
    if inp<100:
        print("try again")
        continue
    else:
        print("congrats")
        break
