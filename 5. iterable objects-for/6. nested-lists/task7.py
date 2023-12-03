n, m = map(int, input().split())
a = []

for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)

for i in range(n):
    sumr = 0
    for z in range(m):
        sumr += a[i][z]
    print(sumr, end=' ')
print()

for i in range(m):
    sumc = 0
    for z in range(n):
        sumc += a[z][i]
    print(sumc, end=' ')
