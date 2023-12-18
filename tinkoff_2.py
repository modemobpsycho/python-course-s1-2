def max_remaining_money(m, n, gifts):
    remaining_money = m

    for i in range(n):
        if gifts[i] <= remaining_money:
            remaining_money -= gifts[i]
        else:
            break  # если не хватает денег на текущий подарок, прекращаем покупки

    return remaining_money


n, m = map(int, input().split())
gifts = list(map(int, input().split()))

result = max_remaining_money(m, n, gifts)
print(result)
