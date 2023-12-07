n = int(input())
res = 1
while n > 0:
    res *= n % 10
    n = n // 10

print(res)
