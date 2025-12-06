# Q36: Write a program that reads the file containing texts and counts the number of whitespaces.

filename = input("Enter filename: ")
with open(filename, "r") as f:
    text = f.read()
num_whitespaces = sum(1 for c in text if c.isspace())
print("Number of whitespaces:", num_whitespaces)
