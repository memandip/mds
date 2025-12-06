# Q30: Create a class Distance containing instance variables feet and inches.
# The class also contains instance methods add() and compare() to add and compare two distance objects respectively.
# Use this class to create two different distance objects and add and compare these two distance objects.

class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def add(self, other):
        total_inches = self.inches + other.inches
        total_feet = self.feet + other.feet + total_inches // 12
        inches = total_inches % 12
        return Distance(total_feet, inches)

    def compare(self, other):
        self_total = self.feet * 12 + self.inches
        other_total = other.feet * 12 + other.inches
        if self_total > other_total:
            return "First distance is greater"
        elif self_total < other_total:
            return "Second distance is greater"
        else:
            return "Both distances are equal"

    def display(self):
        print(f"{self.feet} feet {self.inches} inches")

print("Enter first distance:")
f1 = int(input("Feet: "))
i1 = int(input("Inches: "))
d1 = Distance(f1, i1)

print("Enter second distance:")
f2 = int(input("Feet: "))
i2 = int(input("Inches: "))
d2 = Distance(f2, i2)

d3 = d1.add(d2)
print("Sum of distances:")
d3.display()
print(d1.compare(d2))
