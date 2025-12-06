# Q5: Write a program to calculate discount on the basis of following assumption:
# a) If purchased amount is greater than or equal to 5000, discount is 10%
# b) If purchased amount is greater than or equal to 4000 and less than 5000, discount is 7%
# c) If purchased amount is greater than or equal to 3000 and less than 4000, discount is 5%
# d) If purchased amount is greater than or equal to 2000 and less than 3000, discount is 3%
# e) If purchased amount is less than 2000, discount is 2%
amount = float(input("Enter purchased amount: "))
if amount >= 5000:
    discount = amount * 0.10
elif amount >= 4000:
    discount = amount * 0.07
elif amount >= 3000:
    discount = amount * 0.05
elif amount >= 2000:
    discount = amount * 0.03
else:
    discount = amount * 0.02
print("Discount:", discount)
print("Net amount:", amount - discount)
