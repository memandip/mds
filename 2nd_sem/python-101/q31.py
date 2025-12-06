# Q31: Create a class Student with instance variables name, roll_number, and marks in five subjects.
# Add three instance methods in this class to calculate total(), percentage(), and division() of the marks obtained by the students.
# Use this class to find total marks obtained, percentage, and division of five students.

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks  # list of 5 marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def division(self):
        pct = self.percentage()
        if pct >= 80:
            return "Distinction"
        elif pct >= 60:
            return "First"
        elif pct >= 45:
            return "Second"
        elif pct >= 32:
            return "Third"
        else:
            return "Fail"

students = []
for i in range(5):
    print(f"Enter details for student {i+1}:")
    name = input("Name: ")
    roll = input("Roll Number: ")
    marks = []
    for j in range(5):
        marks.append(float(input(f"Marks in subject {j+1}: ")))
    students.append(Student(name, roll, marks))

for s in students:
    print(f"\nStudent: {s.name}, Roll: {s.roll_number}")
    print("Total:", s.total())
    print("Percentage:", s.percentage())
    print("Division:", s.division())
