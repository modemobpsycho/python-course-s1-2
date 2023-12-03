from string import ascii_uppercase

n = int(input())

print([j[i] for i in range(n) for j in ascii_uppercase.split()])
