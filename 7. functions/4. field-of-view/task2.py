value = 10


def foo():
    global value
    value = 5
    value += 1


print(value)
