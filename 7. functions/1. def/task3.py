def sum_num(stroka):
    total = 0
    for i in list(stroka):
        if i.isdigit():
            total += int(i)
    print(total)
