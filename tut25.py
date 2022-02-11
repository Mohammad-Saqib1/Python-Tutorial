#Enumerate function
l1=["Bhindi","Aloo","Chowmin","Chopstiks"]
i=1
for line in l1:
    if i%2 is 1:
        print(f"jarvis please buy {line}")
    i+=1
for index,item in enumerate(l1):
    if index%2==0:
        print(f"jarvis please buy {item}")