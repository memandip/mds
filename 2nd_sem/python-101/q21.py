# Q21: Write a program to find product of two matrices.
# Assumes both matrices are 2x2 for simplicity.
print("Enter elements for first 2x2 matrix:")
matrix1 = [[int(input(f"Element [{i+1}][{j+1}]: ")) for j in range(2)] for i in range(2)]
print("Enter elements for second 2x2 matrix:")
matrix2 = [[int(input(f"Element [{i+1}][{j+1}]: ")) for j in range(2)] for i in range(2)]
result = [[0 for _ in range(2)] for _ in range(2)]
for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
print("Product of matrices:")
for row in result:
    print(row)
