
#PALINDROME NUMBER
def next_palindrome(n):

    n=n+1
    while not is_palindrome(n):
        n+=1
    return n
def is_palindrome(n):
    return str(n)==str(n)[::-1]

try:
    bcz=" "
    while(bcz!="c" and bcz!="q"):
    
        if __name__ == "__main__":
            n=int(input("Enter the how much value which you want to palindrome"))
            numbers=[]
            for i in range(n):
                numbers.append(int(input("Enter the number")))
            for i in range(n):
                print(f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")
        txt=input("Please enter q for quit and c for continue")
        if txt=="c":
            continue
        elif txt=="q":
            exit()
except Exception as e:
    print(e,"Please Enter only integer value")