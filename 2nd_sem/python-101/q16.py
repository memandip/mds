# Q16: Write a program to check if a number is Armstrong Number or not.
num = int(input("Enter a number: "))
digits = [int(d) for d in str(abs(num))]
power = len(digits)
armstrong_sum = sum([d ** power for d in digits])
if num == armstrong_sum:
    print("Armstrong number")
else:
    print("Not Armstrong number")
