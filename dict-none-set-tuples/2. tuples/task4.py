n = int(input())
c = []
for i in range(n, n**2 + 1):
    if i % 2 != 0:
        c.append(i)
print(tuple(c))
