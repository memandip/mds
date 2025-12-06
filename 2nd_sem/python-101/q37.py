# Q37: Write a program to find sum and average of numbers stored in a file. Create a separate file to write output.

input_file = input("Enter input filename: ")
output_file = input("Enter output filename: ")

with open(input_file, "r") as f:
    numbers = [float(line.strip()) for line in f if line.strip()]

total = sum(numbers)
average = total / len(numbers) if numbers else 0

with open(output_file, "w") as f:
    f.write(f"Sum: {total}\n")
    f.write(f"Average: {average}\n")

print("Output written to", output_file)
