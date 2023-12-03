n = int(input())
for i in range(n):
    a = input()
    if len(a) > 10:
        b = a[0]
        c = a[-1]
        d = a[1:-2]
        a = b + str(len(d)+1) + c
    print(a)
