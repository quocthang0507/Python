matrix = [2, 3, 9], [5, 4, 6], [1, 8, 7]

print(matrix)

for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 3-j-1):
            if matrix[i][k] > matrix[i][k+1]:
                matrix[i][k], matrix[i][k+1] = matrix[i][k+1], matrix[i][k]

print(matrix)
