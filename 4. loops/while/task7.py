Xkm, Ykm = map(float, input().split())
days = 1
while Xkm <= Ykm:
    Xkm = Xkm + Xkm*0.15  # Получаем сколько пробежал в следующий день +15%
    days = days + 1       # Увеличиваем счетчик дней
print(days)
