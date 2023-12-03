n, m = map(int, input().split())
count = 0

for a in range(n+1):
    for b in range(m+1):
        if a + b ** 2 == m and a ** 2 + b == n:
            count += 1
print(count)
