import abc 
from abc import *

class Shape(ABC):
    def area(self):
        pass

class Rectangle(Shape):
    def area(self, l, w):
        return l * w

class Triangle(Shape):
    def area(self, b, h):
        return (1/2) * b * h

class Square(Shape): 
    def area(self, s):
        return s**2
    
r = Rectangle()
print("The area of Rectangle is: ",r.area(2, 4))

t = Triangle()
print("The area of Triangle is: ",t.area(2, 4))

s = Square()
print("The area of Square is: ",s.area(6))