a = int(input())
# если делится на 15 без остатка значит это число делится и на 3 и на 5
if a % 15 == 0:
    print('FizzBuzz')
elif a % 3 == 0:
    print('Fizz')
elif a % 5 == 0:
    print('Buzz')
else:
    print(a)

