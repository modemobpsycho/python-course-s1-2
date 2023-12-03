s = []
flag = "Yes"
for i in range(4):
    s.append(list(input()))

for i in range(3):
    for j in range(3):
        if s[i][j] == s[i][j+1] == s[i+1][j] == s[i+1][j+1]:
            flag = "No"
print(flag)
