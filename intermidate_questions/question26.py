# 26. Matrix Diagonal Sum

# Question: Find the sum of the primary and secondary diagonals of a square matrix.

# Answer:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


n = len(matrix)


primary = 0
secondary = 0


for i in range(n):
    primary += matrix[i][i]
    secondary += matrix[i][n - 1 - i]


print("Primary diagonal:", primary)
print("Secondary diagonal:", secondary)