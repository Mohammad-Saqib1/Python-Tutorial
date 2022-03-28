#function caching
import time
from functools import lru_cache
@lru_cache(maxsize=2)
def some_work(n):
    time.sleep(n)
    return n
if __name__ == "__main__":
    print("Now running some work")
    some_work(3)
    some_work(3)
    some_work(3)
    some_work(3)

    print("Done___running some work")
    some_work(3)
    print("Called again")
    some_work(3)
    print("Called again and agian") 
    some_work(3)
    print("Called again and agian")
    some_work(3)
    print("Called again and agian")