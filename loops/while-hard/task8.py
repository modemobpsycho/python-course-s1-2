a = int(input())
i = 0
while a > 0:
    if a % 10 == 7:
        i = i + 1
    a = a // 10

print(i)
