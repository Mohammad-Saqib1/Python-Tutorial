n=18
n2=1
print("You have only 9 guesses")
while(n2<=9):
    n1=int(input("guess the number"))
    if n1>18:
        print("Please enter small value")
    elif n1<18:
        print("Please enter greater value")
    else:
        print("Congrats! You won")
        print(n2,"He took to finish")
        break
        
    print(9-n2,"no of guesses left")
    n2=n2+1

if (n2>9):
    print("Game over")
