# Q25: Write a program using recursive function to find nth Fibonacci number.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter n: "))
print(f"{num}th Fibonacci number:", fibonacci(num))
