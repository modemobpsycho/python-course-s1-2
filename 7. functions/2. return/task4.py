def first_unique_char(s):
    for i in s.lower():
        if s.count(i) == 1:
            return (s.index(i))
    else:
        return -1


s = input()
print(first_unique_char(s))
