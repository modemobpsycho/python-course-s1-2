totals = int(input())
m = totals // 60  # Делим нацело
s = totals % 60  # получаем остаток от деления
print(f"{totals} сек - это {m} мин. {s} сек.")
