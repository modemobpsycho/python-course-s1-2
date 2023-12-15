text = input()
set_text = set(text)
for i in text:
    if i in set_text:
        print(i, end="")
        set_text.remove(i)
