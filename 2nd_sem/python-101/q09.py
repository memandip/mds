# Q9: The rates of tax on gross salary are as shown below:
# Income Tax
# Less than 10,000 Nill
# Rs. 10,000 to 19,999 10%
# Rs. 20,000 to 39,999 15%
# Rs. 40,000 to above 20%
# Write a program to compute the net salary after deducting the tax for the given information and print the same.

salary = float(input("Enter gross salary: "))
if salary < 10000:
    tax = 0
elif salary < 20000:
    tax = salary * 0.10
elif salary < 40000:
    tax = salary * 0.15
else:
    tax = salary * 0.20
net_salary = salary - tax
print("Tax:", tax)
print("Net Salary:", net_salary)
