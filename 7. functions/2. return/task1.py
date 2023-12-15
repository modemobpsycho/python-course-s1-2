def generate_fizz_buzz_list(number):
    sp = []
    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            sp.append('FizzBuzz')
        elif i % 3 == 0:
            sp.append('Fizz')
        elif i % 5 == 0:
            sp.append('Buzz')
        else:
            sp.append(i)
    return sp
