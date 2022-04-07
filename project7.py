#Fake Multiplication table
import random
def Multiplication(number):
    wrong=random.randint(0,9)
    table=[i*number for i in range(1,11)]
    table[wrong]=table[wrong] + random.randint(0,10)
    return table
def is_correct(table,number):
    for i in range(1,11):
        if table[i-1]!=i*number:
            return i-1
    return None

if __name__ == "__main__":
    abc=" "
    while(abc!="c" and abc!="q"):
        try:
            number=int(input("Enter a number"))
            mytable=Multiplication(number)
            print(mytable)

            wrong_index =is_correct(mytable,number)
            print(f"The table is wrong at index {wrong_index}")
        except Exception as e:
            print("Please Enter a valid number")
        quick=input("Enter q for quit and c for continue")
        if quick=="c":
            continue
        elif quick=="q":
            exit()
        