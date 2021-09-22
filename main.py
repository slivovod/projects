import copy

n = int(input("Введите размер матрицы (n * n): "))
matrix = []
for i in range(n):
    temporary_list_of_vars = []
    for j in range(n):
        temporary_list_of_vars.append(int(input()))
    matrix.append(temporary_list_of_vars)

def minor(matrix, i, j):
    mnr = copy.deepcopy(matrix)
    del mnr[i]
    size = (len(matrix[0]) - 1)
    for i in range(size):
        del mnr[i][j]
    return mnr

def det(matrix):
    n = len(matrix[0])
    if(n > 1):
        determinant = 0
        positive_or_negative = 1
        for j in range(n):
            determinant += matrix[0][j] * positive_or_negative * det(minor(matrix, 0, j))
            positive_or_negative *= -1
        return determinant
    else:
        return matrix[0][0]

"""matrix = [[2, 4, 8, 1, 2],
     [2, 4, 1, 0, 5],
     [2, 7, 1, 2, 6],
     [4, 0, 2, 6, 1],
     [8, 5, 1, 3, 4]]"""

print(det(matrix))
