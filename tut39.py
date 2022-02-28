#multilevel inheritence
class Dad:
    basketball=6
    dance=10
class Son(Dad):
    # dance=1
    basketball=9
    def is_dance(self):
        return f"Yes I dance {self.dance} no of time"
class Grandson(Son):
    # dance=6
    guitar=1
    def is_dance(self):
        return f"Jackson yeah!YES I dance very awesomely {self.dance} no of time"
darry=Dad()
larry=Son()
harry=Grandson()
print(harry.basketball)
print(larry.basketball)

print(harry.is_dance())