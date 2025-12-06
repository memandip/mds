# Q20: Write a program to find sum of two matrices.
# Assumes both matrices are 2x2 for simplicity.
print("Enter elements for first 2x2 matrix:")
matrix1 = [[int(input(f"Element [{i+1}][{j+1}]: ")) for j in range(2)] for i in range(2)]
print("Enter elements for second 2x2 matrix:")
matrix2 = [[int(input(f"Element [{i+1}][{j+1}]: ")) for j in range(2)] for i in range(2)]
result = [[matrix1[i][j] + matrix2[i][j] for j in range(2)] for i in range(2)]
print("Sum of matrices:")
for row in result:
    print(row)
