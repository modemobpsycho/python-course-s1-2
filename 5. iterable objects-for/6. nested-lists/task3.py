n = int(input())
a = []
for j in range(n):
    a.append(list(input().split()))

for i in range(n):
    for j in range(n):
        print(a[n-1-j][n-1-i], end=" ")
    print()
