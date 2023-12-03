n = int(input())
count_numbers = 0
dividers = 0

for p in range(n + 1, 2 * n):
    for k in range(2, int(p ** 0.5) + 1):
        if p % k == 0:
            dividers += 1
            break
    if dividers == 0:
        count_numbers += 1
    dividers = 0

print(count_numbers)
