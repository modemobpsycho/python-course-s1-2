a = input().lower()
b = input().lower()
a1 = a[-1]
b1 = b[0]
if a1 == b1:
    print('Good')
elif a[-1] == 'ь':
    if a[-2] == b1:
        print('Good')
    else:
        print('Bad')
else:
    print('Bad')
