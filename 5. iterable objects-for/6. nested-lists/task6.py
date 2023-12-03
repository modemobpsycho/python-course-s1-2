c = []
for i in range(5):
    c.append(list(map(int, input().split())))

for i in range(5):
    for j in range(5):
        if c[i][j] == 1:
            a = i
            b = j

с = abs(a-2) + abs(b-2)
print(с)
