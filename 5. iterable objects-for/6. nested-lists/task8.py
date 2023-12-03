n = int(input())
m = []
for i in range(n):
    l = list(input().split())
    m.append(l)
flag = True
for i in range(n):
    if not flag:
        break
    for j in range(n):
        if i != j:
            if m[i][j] != m[j][i]:
                flag = False
                break

print('Yes' if flag else 'No')
