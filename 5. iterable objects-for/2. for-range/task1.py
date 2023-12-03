from random import randint

s = 0

for i in range(3):
    a = randint(1, 10)
    s += a
    print(a, end=" ")
print(s)
