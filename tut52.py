#corounties
def searcher():
    import time
    book="This is a book"
    time.sleep(4)
    while True:
        text=(yield)
        if text in book:
            print("your text is in book")
        else:
            print("text is not in book")
search= searcher()
print("search started")
next(search)
print("next method run")
search.send("harry")
# search.close()
# search.send("like ths video")
# input("press any key")