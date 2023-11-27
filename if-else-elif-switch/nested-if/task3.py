a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print(a)
else:
    if a < b and c < b:
        print(b)
    else:
        print(c)
