text = input().lower()
text_set = set(text)
if len(text_set) == 26:
    print('YES')
else:
    print('NO')
