# Q3: Write a program to calculate discount on the basis of following assumption:
# a) If purchased amount is greater than or equal to 1000, discount is 5%
amount = float(input("Enter purchased amount: "))
if amount >= 1000:
    discount = amount * 0.05
else:
    discount = 0
print("Discount:", discount)
print("Net amount:", amount - discount)
