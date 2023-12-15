def count_letters(text):
    upper = 0
    lower = 0
    for i in text:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    print(f'Количество заглавных символов: {upper}')
    print(f'Количество строчных символов: {lower}')
