n = int(input())
l = list(map(int, input().split()))
cnt = 0
for i in range(0, n - 1):
    flag = False

    for j in range(n - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
            cnt += 1
            flag = True
    if not flag:
        break
print(*l, '\n'+str(cnt))
