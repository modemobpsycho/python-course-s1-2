b = [6, 5, 2, 9]
print(sorted(b))
print(sorted(b, reverse=True))
# сам список b не изменился
print(b)
# теперь изменим b
b = sorted(b)
print(b)
