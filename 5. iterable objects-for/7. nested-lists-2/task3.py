n = int(input()) 
mas = []
for i in range(n):
    mas.append(list(map(int, input().split()))) 
count_match = 0
for i in range(n):  
    for j in range(n):
        if mas[i][0] == mas[j][1]:
            count_match += 1
print(count_match)
