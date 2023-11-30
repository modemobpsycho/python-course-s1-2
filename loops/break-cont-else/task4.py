a = input()
while len(a) > 0:
    if a[0] == 'a' or a[0] == 'e': 
        print('Ага! Нашлась')
        break
    print(f'Текущая буква: {a[0]}')
    a = a[1::]       
else:
    print('Распечатали все буквы') 