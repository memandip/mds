# Q27: Create a class Circle containing an instance variable radius.
# The class also contains two instance methods area() and circumference() to find area and circumference of circles respectively.
# Use this class to find area and circumference of two different circles. Use PI as a class variable.

class Circle:
    PI = 3.141592653589793

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius ** 2

    def circumference(self):
        return 2 * Circle.PI * self.radius

circle1 = Circle(float(input("Enter radius of circle 1: ")))
circle2 = Circle(float(input("Enter radius of circle 2: ")))

print("Circle 1 - Area:", circle1.area(), "Circumference:", circle1.circumference())
print("Circle 2 - Area:", circle2.area(), "Circumference:", circle2.circumference())
