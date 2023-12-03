pairs = {'()', '[]', '{}'}
str = input().replace(' ', '')

for _ in range(len(str)//2):
    for i in pairs:
        str = str.replace(i, '')

if len(str) == 0:
    print('YES')
else:
    print('NO')
