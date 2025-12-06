# Q8: Admission to a professional course is subject to the following conditions:
# a) Marks in mathematics >=60
# b) Marks in physics >=50
# c) Marks in chemistry >=40
# d) Total in all three subjects >=200
# Or
# Total in mathematics and physics >=150
# Given the marks in three subjects, write a program to process the applications to list eligible candidates.

math = int(input("Enter marks in Mathematics: "))
physics = int(input("Enter marks in Physics: "))
chemistry = int(input("Enter marks in Chemistry: "))

total = math + physics + chemistry
math_physics = math + physics

if (math >= 60 and physics >= 50 and chemistry >= 40 and total >= 200) or (math_physics >= 150):
    print("Eligible")
else:
    print("Not eligible")
