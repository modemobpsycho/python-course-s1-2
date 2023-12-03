n, m = map(int, input().split())
matrix = []
mt = 0
с = 0

for i in range(n):
    k = list(map(int, input().split()))
    matrix.append(k)

for i in range(n):
    for j in range(m):
        if matrix[i][j] > mt:
            mt = matrix[i][j]

for row in range(n):
    if mt in matrix[row]:
        с += 1

print(с)
