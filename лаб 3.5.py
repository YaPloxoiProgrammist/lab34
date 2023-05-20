def transpose(matrix):
    m = len(matrix)
    n = len(matrix[0])
    nw_list = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            nw_list[i][j] = matrix[j][i]
    return nw_list
matrix = []
while True:
    variable = input()
    if variable == '0':
        break
    else:
        matrix.append(variable.split())
print(transpose(matrix))