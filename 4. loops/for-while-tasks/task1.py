x = int(input())
minimum, maximum = 9, 0

while x:
    x, n = divmod(x, 10)
    minimum = min(minimum, n)
    maximum = max(maximum, n)

print(minimum)
print(maximum)
