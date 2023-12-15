numbers = list(map(int, input()))

for index, value in enumerate(numbers):
    if index % 2 == 0:
        if value * 2 > 9:
            numbers[index] = value * 2 - 9
        else:
            numbers[index] = value * 2
if sum(numbers) % 10 == 0:
    print('True')
else:
    print('False')
