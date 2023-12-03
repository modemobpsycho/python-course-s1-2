s = input()
sum = 0
cnt = 0
for i in (s):
    if ("0" <= i <= "9"):
        sum += int(i)
        cnt += 1

print(cnt, sum)
