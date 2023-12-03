n = int(input())
M = 0
C = 0
for i in range(n):
    m, c = map(int, input().split())
    if m > c:
        M += 1
    elif m < c:
        C += 1
if M > C:
    print('Mishka')
elif M < C:
    print('Chris')
else:
    print('Friendship is magic!^^')
