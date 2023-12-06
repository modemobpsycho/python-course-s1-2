list_inp = list(map(int, input().split()))
dic = {}
x = len(list_inp) - 1
while x != 0:
    if len(dic) == 0:
        dic = {list_inp[x - 1]: list_inp[x]}
    else:
        dic = {list_inp[x - 1]: dic}
    x -= 1
print(dic)
