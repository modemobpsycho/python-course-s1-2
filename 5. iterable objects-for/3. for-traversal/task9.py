x = list(input().lower())
y = []
for i in x:
    y.append(x.count(i))

print(max(y))
