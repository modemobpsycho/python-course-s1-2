n = int(input())
s = 0
for i in range(n):
    a = int(input())
    s += a
    print("current s:", s)

print("total", s)
print("average =", s/n)
