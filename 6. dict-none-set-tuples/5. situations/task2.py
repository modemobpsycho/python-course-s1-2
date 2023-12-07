s = input().lower()

d = {}
for i in s:
    if i.isalpha():
        d[i] = d.get(i, 0) + 1
print(d)
