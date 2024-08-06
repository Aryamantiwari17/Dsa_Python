##polymorphism with functions and methods

##base class
import math

class Shape:
    def area(self):
        return "the area of the figure"
    


##derived class 1
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):##overriden the function
        return self.width*self.height
    

class Circle(Shape):
    def __init__(self,raduis):
        self.raduis=raduis

    def area(self):## we again goona override  this function again
        return (3.14*self.raduis*self.raduis)
    

    ##function that demonstrates the polymorphism

def print_area(shape):
        print(f"The area is {shape.area()}")


rectangle=Rectangle(4,5)

circle=Circle(4)
print(rectangle.area())
print(circle.area())
print_area(rectangle)
print_area(circle)






    








