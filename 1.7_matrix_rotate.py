
# O(1) space O(n^2) where n is the length of the matrix
def rotate90(matrix):
    transpose(matrix)

    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]

    pass




def transpose(matrix):
    width = len(matrix) # if n x n

    for i in range(width):
        for j in range(i, width):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp





x = [[1, 2,3, 4, 5, 6, 7, 8],
     [11, 12, 13, 14, 15, 16, 17, 18],
     [21, 22, 23, 24, 25, 26, 27, 28],
     [31, 32, 33, 34, 35, 36, 37, 38],
     [41, 42, 43, 44, 45, 46, 47, 48],
     [51, 52, 53, 54, 55, 56, 57, 58],
     [61, 62, 63, 64, 65, 66, 67, 68],
     [71, 72, 73, 74, 75, 76, 77, 78],
     ]


rotate90(x)
rotate90(x)
rotate90(x)
rotate90(x)

for row in x:
    print(row)