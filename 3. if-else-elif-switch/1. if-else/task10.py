# приводим полученные числа в массив и сортируем его по возрастанию
numbers = [int(input()), int(input()), int(input())]
numbers.sort()
# если сумма двух наименьших сторон больше 3 стороны
if sum(numbers[:-1]) > numbers[-1]:
    print('YES')
else:
    print('NO')
