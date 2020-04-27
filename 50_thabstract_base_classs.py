from abc import ABC , abstractmethod
# note :- we can not make object with thebaseclass i.e shape
class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class ractangle(shape):
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath
    def printarea(self):
        return f"The area of ractangle is;- {self.length*self.breath}"
    def __repr__(self):
        return f"ractangle({self.length},{self.breath})"
angle = ractangle(4,5)
print(angle.printarea())
print(angle)
#
# as i ention on thetop of code that wecannot make object of base class i.e shape if i try the see what will happen
# #   File "50thabstractbasecls.py", line 19, in <module>
#     shapeobj = shape()
# TypeError: Can't instantiate abstract class shape with abstract methods printarea
# we get this error
shapeobj = shape()
print(shapeobj)
