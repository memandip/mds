# Q18: Write a program to find smallest and largest number among 10 numbers stored in a list.
numbers = []
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)
smallest = min(numbers)
largest = max(numbers)
print("Smallest number:", smallest)
print("Largest number:", largest)
