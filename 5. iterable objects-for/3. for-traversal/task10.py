l = list(map(int, input()))
chet = 0
nechet = 0
for i in range(len(l)):
    if (i) % 2 == 0:
        chet += l[i]
    else:
        nechet += l[i]

if (nechet-chet) % 11 == 0:
    print('YES')
else:
    print('NO')
