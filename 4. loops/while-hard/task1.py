s = 0
# Запускаем бесконечный цикл
while True:
    n = int(input())
    if n == 0:
        break     # Выходим из цикла как только встречается 0
    s += n
print(s)
