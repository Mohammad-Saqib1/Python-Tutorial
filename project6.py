#Search Engine

sentences = ["python is a good", "This is a good language",
             "i lke python", "python is a perfect programming language"]
results=[]
def search():
    word=input("Enter what  do you want to search")
    for item in sentences:
        if word.lower() in item.lower():
            results.append(item)
    if len(results)==0:
        print("Sorry the item you searched is not available")
    else:
        print(f"{len(results)} results found for {word}")
            
        for i in results:
            print(i)
search()
