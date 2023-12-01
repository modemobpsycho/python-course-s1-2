# так как на входе Два вещественных числа то спользуем float
a = float(input())
b = float(input())
c = input()
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b == 0:
        print('Неизвестно')
    else:
        print(a / b)
else:
    print('Неизвестно')

