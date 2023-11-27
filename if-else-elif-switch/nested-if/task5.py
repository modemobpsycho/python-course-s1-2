a, b, c = map(int, input().split())
if a > b and a > c:
    if b > c:
        print(a-c)
    else:
        print(a-b)
else:
    if b > a and b > c:
        if a > c:
            print(b-c)
        else:
            print(b-a)
if c > a and c > b:
    if b > a:
        print(c-a)
    else:
        print(c-b)
