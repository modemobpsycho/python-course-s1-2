def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n = int(input())
s = int(input())
for i in range(n - 1):
    b = int(input())
    s = gcd(s, b)
print(s)
