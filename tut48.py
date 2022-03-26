# #comprehension
# dict1={i for i in range(100) if i%3==0}
dict1={i:f"item{i}" for i in range(100) if i%3==0}
#in reverse mode
dict2={value:key for key,value in dict1.items()}
# print(dict2)
# dresses=[dress for dress in ["dress1","dress2","dress1","dress2"]]
# dresses={dress for dress in["dress1","dress2","dress1","dress2"]}
# print(type(dresses))
# print(dresses)
# by genetors iteration
evens=(i for i in range(100) if i%2==0)
print(evens.__next__())
# for item in evens:
#     print(item)
#same work by coprehension if you use comprehension {} must use
evens={i for i in range(100) if i%2==0}
print(evens)