# Q33: Overload + operator in Q.N.30 to add two distance objects.

class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = self.inches + other.inches
        total_feet = self.feet + other.feet + total_inches // 12
        inches = total_inches % 12
        return Distance(total_feet, inches)

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

d3 = d1 + d2
print("Sum of distances using + operator:")
d3.display()
