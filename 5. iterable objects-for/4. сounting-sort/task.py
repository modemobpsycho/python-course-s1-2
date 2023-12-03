a = list(map(int, str(input())))
count = [0]*10
for i in a:

    count[i] += 1
for i in range(10):
    if count[i] > 0:
        print(i, count[i])
