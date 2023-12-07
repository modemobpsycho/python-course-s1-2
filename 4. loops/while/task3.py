l, b = map(int, input().split())
year = 0
# Пока вес лима будет меньше веса боба бежим по циклу и вычисляем их вес
# Один цикл это один год
while l <= b:
    l = l * 3
    b = b * 2
    year += 1

print(year)
