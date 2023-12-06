n = int(input())
arhiv = {}
for i in range(n):
    a = input()
    if a not in arhiv:
        arhiv[a] = 1
        print('OK')
    else:
        print(f'{a}{arhiv[a]}')
        arhiv[a] += 1
