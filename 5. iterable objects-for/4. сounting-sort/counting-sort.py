n = int(input())
a = map(int, input().split())
count = [0] * 201
for i in a:
    count[i] += 1

for i in range(-100, 101):
    for _ in range(count[i]):
        print(i, end=' ')
