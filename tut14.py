#open(),read(),readline()and readlines() etc
#readline():code read line by line
"""
f=open("harry.txt")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()
#it is use for print all lines

f=open("harry.txt")
content=f.read()
print(content)
f.close()
"""
# It is use for print character by character
"""
f=open("harry.txt")
content=f.read()
for line in content:
    print(line,end=" ")
    
  
f.close()
"""
# It is use for print all lines which available in file
f=open("harry.txt","rt")

for line in f:
    print(line)
f.close()    
#It is use for print character which you needed
f=open("harry.txt")
content=f.read(15)
print(content)
f.close()

