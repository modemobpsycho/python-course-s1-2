n, m = map(int, input().split())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
for i in range(n-2, -1, -1):
    for j in range(m-2, -1, -1):
        if matrix[i][j] == 0 and matrix[i+1][j] != 0 and matrix[i][j+1] != 0:
            matrix[i][j] = matrix[i+1][j] + matrix[i][j+1]
for row in matrix:
    print(' '.join(map(str, row)))
