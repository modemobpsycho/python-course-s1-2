from math import ceil
l, w, h = map(int, input().split())
P = 2 * (l * h) + 2 * (w * h)
A = P / 16
print(ceil(A))
