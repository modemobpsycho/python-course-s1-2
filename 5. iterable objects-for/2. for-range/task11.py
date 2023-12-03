n = int(input())
for i in range(n):
    a = input().lower()
    ind = a.find('рок') + 1
    if ind > 0:
        print(i + 1, ind)
