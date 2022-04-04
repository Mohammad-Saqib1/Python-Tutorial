#json module
import json
data={"var1":"harry","var2":"56"}
print(data)
# if you want to print a single value of string
parsed=json.loads(data)
print(parsed['var1'])
print(type(parsed))

#if you want to make python file to js

data2={"channel":"CWH","cars":['bmw','audi','ferreri'],"fridge":('rot',540),"isbad":False}
jscomp=json.dumps(data2)
print(jscomp)