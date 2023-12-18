
def shift_letter(letter: str, shift: int) -> str:
    'Функция сдвигает символ letter на shift позиций'
    return chr((ord(letter) - 97 + shift) % 26 + 97)
