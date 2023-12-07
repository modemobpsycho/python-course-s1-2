s = input().lower()

d = {}
for i in s:
    if i.isalpha():
        d[i] = d.get(i, 0) + 1

s2 = input().lower()

d2 = {}
for i in s2:
    if i.isalpha():
        d2[i] = d2.get(i, 0) + 1
if d == d2:
    print('YES')
else:
    print('NO')
