n = int(input())
c = 1
sum = 0

while c <= n:
    if n % c == 0:

        sum += c
    c += 1
print(sum)
