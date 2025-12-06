# Q22: Write a program using list comprehension to find sum of only even numbers.
numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
even_sum = sum([n for n in numbers if n % 2 == 0])
print("Sum of even numbers:", even_sum)
