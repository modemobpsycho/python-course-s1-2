n, m = map(int, input().split())
c = []
a = 0
i_max = 0
j_max = 0

for i in range(n):
    l = list(map(int, input().split()))
    c.append(l)

for i in range(n):
    for j in range(m):
        if c[i][j] > a:
            a = c[i][j]
            i_max = i
            j_max = j
print(a)
print(i_max, j_max)
