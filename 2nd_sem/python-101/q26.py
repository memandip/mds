# Q26: Create a class Rectangle containing instance variables length and breadth.
# The class also contains two instance methods area() and perimeter() to find area and perimeter of rectangles respectively.
# Use this class to find area and perimeter of two different rectangles.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

rect1 = Rectangle(float(input("Enter length of rectangle 1: ")), float(input("Enter breadth of rectangle 1: ")))
rect2 = Rectangle(float(input("Enter length of rectangle 2: ")), float(input("Enter breadth of rectangle 2: ")))

print("Rectangle 1 - Area:", rect1.area(), "Perimeter:", rect1.perimeter())
print("Rectangle 2 - Area:", rect2.area(), "Perimeter:", rect2.perimeter())
