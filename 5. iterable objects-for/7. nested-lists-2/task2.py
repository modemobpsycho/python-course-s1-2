n = int(input())
a, b, c = map(int, input().split())
matrix = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            matrix[i][j] = a
        elif i > j:
            matrix[i][j] = b
        else:
            matrix[i][j] = c
for row in matrix:
    print(*row)
