# 25. Matrix Transpose

# Question: Find the transpose of a matrix.

# Answer:

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]


transpose = []


for col in range(len(matrix[0])):
    row = []


    for row_index in range(len(matrix)):
        row.append(matrix[row_index][col])


    transpose.append(row)


print(transpose)