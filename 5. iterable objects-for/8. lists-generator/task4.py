n = int(input())
number_list = []

for i in range(n, n*n+1):
    if i % 2 != 0:
        number_list.append(i)

print(number_list)
