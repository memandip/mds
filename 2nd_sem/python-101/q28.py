# Q28: Create a class Box with instance variables width, height and depth.
# The class also contains instance methods volume() and surface_area() to find volume and surface area of boxes respectively.
# Use this class to find volume and surface area of two different boxes.

class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def volume(self):
        return self.width * self.height * self.depth

    def surface_area(self):
        return 2 * (self.width * self.height + self.height * self.depth + self.width * self.depth)

box1 = Box(float(input("Enter width of box 1: ")), float(input("Enter height of box 1: ")), float(input("Enter depth of box 1: ")))
box2 = Box(float(input("Enter width of box 2: ")), float(input("Enter height of box 2: ")), float(input("Enter depth of box 2: ")))

print("Box 1 - Volume:", box1.volume(), "Surface Area:", box1.surface_area())
print("Box 2 - Volume:", box2.volume(), "Surface Area:", box2.surface_area())
