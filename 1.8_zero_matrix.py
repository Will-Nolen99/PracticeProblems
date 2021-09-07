

# O(m * n ) time
# O(m + n) space
def zero_matrix(matrix):
    height = len(matrix)
    width = len(matrix[0])

    columns = []
    rows = []

    for y in range(height):
        for x in range(width):
            if matrix[y][x] == 0:
                rows.append(y)
                columns.append(x)

    for i in columns:
        for j in range(height):
            matrix[j][i] = 0

    for i in rows:
        for j in range(width):
            matrix[i][j] = 0




x = [[1, 1, 1, 0, 1],
     [1, 0, 1, 1, 1],
     [1, 1, 1, 1, 1]]

zero_matrix(x)
for row in x:
    print(row)