text = input()
set_text = set()
for i in text:
    if i.isdigit() and text.count(i) > 1:
        set_text.add(i)
if len(set_text) >= 1:
    print(*sorted(set_text))
else:
    print('NO')
