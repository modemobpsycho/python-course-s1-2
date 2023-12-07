password = input()
# Если пароль от 5 до 9 символов то то запоминаем его и проверяем следующий введеный пароль
while 5 <= len(password) <= 9:
    valid_password = password
    password = input()
print(valid_password)
