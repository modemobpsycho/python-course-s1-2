parol_1, parol_2 = input(), input()
# проверяем длину первого пароля и сравниваем первый пароль со вторым
if len(parol_1) >= 7 and parol_1 == parol_2:
    print('OK')
# иначе проверяем длину первого пароля
elif len(parol_1) < 7:
    print('Short')
# иначе проверяем равен первый пароль второму или нет
elif parol_1 != parol_2:
    print('Difference')

