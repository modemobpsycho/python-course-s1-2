count = int(input())
result = ""
for _ in range(count):
    s = input()
    if 'соль' in s:
        continue
    result += s + ', '

print(result[:-2])
