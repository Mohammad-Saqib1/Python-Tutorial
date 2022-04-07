#if you want to reverse any hotel list please check it
# print("Enter the number of the list")
if __name__ == "__main__":
    
    try:
        size=int(input("Enter the size of the list"))
        mylist=[]
        for i in range(size):
          mylist.append(int(input("Enter the element of list")))
        print(f"The given list is {mylist}")
        reverse=mylist[:]
        reverse.reverse()
        print(f"The reverse list is{reverse}")
        reverse1=mylist[::-1]
        print(f"Second reverse list is {reverse1}")
    except Exception as e:
        print(e,"Please enter only integer value")

    
