n = int(input())
count = 0
while True:
    if n == 1:
        break
    count += 1
    if n % 2 == 0:
        n = n/2
    else:
        n = 3*n+1

print(count)
