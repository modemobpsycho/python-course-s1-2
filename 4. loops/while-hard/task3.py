n = int(input())  # n - общий объем рюкзака
a = 0             # a - объем который уже занят
e = 0             # e - обьем следующей строки
b = 0             # b - колличество
while a <= n:
    e = int(input())
    b = b + 1
    a += e
print('Довольно!')
print(a - e)
print(b - 1)
