n, m = map(int, input().split())
matrix = []
mx = 0
l = []

for i in range(n):
    k = list(map(int, input().split()))
    matrix.append(k)

for i in range(n):
    for j in range(m):
        if matrix[i][j] > mx:
            mx = matrix[i][j]

for i in range(n):
    if mx in matrix[i]:
        l.append(sum(matrix[i]))
    else:
        l.append(0)

print(l.index(max(l)))
