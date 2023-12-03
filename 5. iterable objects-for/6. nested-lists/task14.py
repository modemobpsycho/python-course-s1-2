n, m = map(int, input().split())
a = []                 
s = []                    

for i in range(n):         
    a.append(input())

input()                    

for j in range(n):
    s.append(input())

countE = 0                 
for i in range(n):
    for j in range(m):
        if a[i][j] == s[i][j]: 
            countE += 1        
print(countE)
