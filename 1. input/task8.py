a, b, c = int(input()), int(input()), int(input())
x1 = a + b + c
x2 = a * b * c
x3 = (a+b) * c
x4 = a * (b+c)
print(max(x1, x2,x3,x4))