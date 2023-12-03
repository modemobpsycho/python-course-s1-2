a = input().split()
a, b = a[0], a[1]
c = []
for i in range(int(a)):
    c.append(list(map(int, input().split())))

for i in range(0, int(a)):
    if i != 0:
        for j in range(1, int(b)):
            c[i][j] = int(c[i][j-1])+int(c[i-1][j])
for i in range(len(c)):
    a = c[i]
    a = " ".join(map(str, a))
    print(a)
