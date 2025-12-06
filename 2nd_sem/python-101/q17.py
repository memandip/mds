# Q17: Write a program to count number of vowels in a string.
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in s if char in vowels)
print("Number of vowels:", count)
