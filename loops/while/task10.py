a = int(input())
counter = 0
while a >= 2:
    a -= 2 ** counter
    counter += 1
print(counter if a == 1 else 'НЕТ')
