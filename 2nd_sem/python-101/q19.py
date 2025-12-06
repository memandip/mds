# Q19: Write a program to count even numbers and odd numbers stored in a list.
numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
even_count = sum(1 for n in numbers if n % 2 == 0)
odd_count = sum(1 for n in numbers if n % 2 != 0)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
