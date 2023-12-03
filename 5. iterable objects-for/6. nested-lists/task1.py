n = int(input())

a = []
s = 0

for i in range(n):
    b = []
    b = list(map(int, input().split()))
    a.append(b)
for i in range(n):
    for j in range(n):
        if i == j:
            s += a[i][j]
print(s)
