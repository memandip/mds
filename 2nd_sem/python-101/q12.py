# Q12: Write a program to find sum and average of 10 numbers stored in a list.
numbers = []
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)
total = sum(numbers)
average = total / 10
print("Sum:", total)
print("Average:", average)
