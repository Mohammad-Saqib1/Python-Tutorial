# recursive and iterative
inp=int(input("Enter the number"))
"""
This is iterative method
 def func(n):
     fact=1
     for i in range(n):
         fact=fact*(i+1)
     return fact
 print(func(inp))
"""
"""
This is recursive method
 def factorial_recursive(n):
     if n==1:
         return 1
     else:
         return n*factorial_recursive(n-1)
 print(factorial_recursive(inp))
"""
"""
calculate fibonacci index
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(inp))
"""
