a, b = map(int, input().split())
print([i**2 if a <= b else i**3 for i in (range(a,b+1) if a <=b else range(a, b - 1, -1))])