import random
def guessgame(a,b,actual):
    guess=int(input(f"Guess the number between {a} and {b}"))
    nguess=1
    while guess!=actual:
        if guess<actual:
            guess=int(input("Plaese enter the bigger value "))
            nguess+=1
        else:
            guess=int(input("Please enter the smaller value"))
            nguess+=1
    print(f"You guesses the number in {nguess}")
    return nguess
if __name__ == "__main__":
    a=int(input("Enter the value of a"))
    b=int(input("Enter the value of b"))
    actual1=random.randint(a,b)
    print("Player 1 turn")
    g1=guessgame(a,b,actual1)
    actual2=random.randint(a,b)
    print("Player 2 turn")
    g2=guessgame(a,b,actual2)
    if g1<g2:
        print("Player 1 won")
    elif g1>g2:
        print("Player 2 won")
    else:
        print("Match tie")
    print(f"The number for player 1 was {actual1} and for player 2 was {actual2}")
    





