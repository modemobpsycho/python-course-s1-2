text = input().lower().split(',')

set_text = set()
for i in text:
    if i not in set_text:
        print("НЕТ")
        set_text.add(i)
    else:
        print('ДА')
