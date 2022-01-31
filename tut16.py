#seek(),tell()
#generally tell() give info that where at my file line character
"""
f=open("harry.txt")
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())

f.close()
"""
#generally seek() is use for reset for our writing file
f=open("harry.txt")
f.seek(3)
print(f.readline())
f.close()