n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
max_value = matrix[0][n-1]
for i in range(1, n):
    j = n - 1 - i
    if matrix[i][j] > max_value:
        max_value = matrix[i][j]
print(max_value)
