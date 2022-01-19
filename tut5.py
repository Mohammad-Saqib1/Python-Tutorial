#dictionary and its functions
d1={}
print(type(d1))
d2={"Harry":"Burger","Ahsan":"Biryani","Gufran":"gym","kamran":"Pratha","Saqib":"Coding"}
print(d2["Saqib"])
print(d2)
d2["Ankit"]="Junk food"
print(d2)

d2[420]="kebbab"
print(d2)

d3=d2
print(d3)
del d3["Saqib"]

d3=d2.copy()
print(d3)

del d3["Harry"]
print(d3)
print(d2)
d3.update({"Leena":"toffee"})
print(d3)
print(d2.keys())
print(d2.items())