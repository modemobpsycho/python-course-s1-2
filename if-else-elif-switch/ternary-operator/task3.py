a, b = int(input()), int(input())
maximum, minimum = (a, b) if a > b else (b, a)
print(minimum, maximum)
