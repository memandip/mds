# Q15: Write a program to check whether a number is palindrome or not.
num = input("Enter a number: ")
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
