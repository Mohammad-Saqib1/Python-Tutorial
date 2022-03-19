#Abstract Base method and @abstractmethod
# from abc import ABCMeta,abstractclassmethod

class Shape(ABC):
    @abstractclassmethod
    def printarea(self):
        return 0
    # def printarea(self):
    #     return 0
class Rect(Shape):
    type="rectangle"
    sides=4
    def __init__(self):
        self.length=6
        self.breadth=7
    def printarea(self):
        return self.length*self.breadth
rec1=Rect()
print(rec1.printarea())
