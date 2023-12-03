n, m = map(int, input().split())
a = []
c = []

for i in range(n):
    l = list(map(int, input().split()))
    a.append(l)
for i in range(n):
    s = 0
    for j in range(m):
        s += a[i][j]
    c.append(s)

print(max(c))
print(c.index(max(c)))
