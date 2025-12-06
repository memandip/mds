# Q14: Write a program to find sum of digits of a number.
num = int(input("Enter a number: "))
total = 0
for digit in str(abs(num)):
    total += int(digit)
print("Sum of digits:", total)
