a = int(input())
h = a // 3600
m = a % 3600 // 60
s = a % 60
print(h, ':',  m // 10, m % 10, ':',  s//10, s % 10, sep='')
