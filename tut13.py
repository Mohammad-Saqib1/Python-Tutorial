#exception handling
print("Enter num1")
num1=input()
print("Enter num2")
num2=input()
#print(num1+int(num2))
#print("This is important line")
try:
    print("The sum of the number",
    num1+int(num2))
except Exception as e:

    print("This is important line")