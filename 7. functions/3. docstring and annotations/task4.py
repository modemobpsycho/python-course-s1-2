def shift_letter(letter: str, shift: int) -> str:
    'Функция сдвигает символ letter на shift позиций'
    return chr((ord(letter) - 97 + shift) % 26 + 97)


def caesar_cipher(letter: str, shift: int) -> str:
    'Шифр цезаря'
    a = ''
    for i in letter:
        if i.isalpha():
            a += shift_letter(i, shift)
        else:
            a += i
    return a
