# Q35: Write a program that reads a text file and writes its output in another text file.
# The output should contain:
# a. Number of letters
# b. Number of digits
# c. Number of other characters

input_file = input("Enter input filename: ")
output_file = input("Enter output filename: ")

with open(input_file, "r") as f:
    text = f.read()

num_letters = sum(1 for c in text if c.isalpha())
num_digits = sum(1 for c in text if c.isdigit())
num_others = sum(1 for c in text if not c.isalpha() and not c.isdigit())

with open(output_file, "w") as f:
    f.write(f"Number of letters: {num_letters}\n")
    f.write(f"Number of digits: {num_digits}\n")
    f.write(f"Number of other characters: {num_others}\n")

print("Output written to", output_file)
