from string import ascii_uppercase
n = int(input())
print([ascii_uppercase[x - 1]*x for x in range(1, n + 1)])
