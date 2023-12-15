def factorial(n):
    if n == 0:
        return 0
    else:
        factor = 1
        for i in range(1, n + 1):
            factor *= i
        return factor


def trailing_zeros(n):
    if n == 0:
        return 0
    else:
        null = 0
        for i in str(factorial(n))[::-1]:
            if i == '0':
                null += 1
            else:
                break
        return null


assert trailing_zeros(0) == 0
assert trailing_zeros(6) == 1
assert trailing_zeros(30) == 7
assert trailing_zeros(12) == 2
print('Проверки пройдены')
