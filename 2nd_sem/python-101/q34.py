# Q34: Write a program that reads a text file and displays the following:
# a. Number of characters
# b. Number of vowels
# c. Number of consonants
# d. Number of words
# e. Number of lines

filename = input("Enter filename: ")
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

with open(filename, "r") as f:
    text = f.read()

num_chars = len(text)
num_vowels = sum(1 for c in text if c in vowels)
num_consonants = sum(1 for c in text if c in consonants)
num_words = len(text.split())
num_lines = text.count('\n') + 1 if text else 0

print("Number of characters:", num_chars)
print("Number of vowels:", num_vowels)
print("Number of consonants:", num_consonants)
print("Number of words:", num_words)
print("Number of lines:", num_lines)
