n, m = map(int, input().split())
u = 0                  

for i in range(n):     
    a = []             
    for j in range(m):  
        a.append(u)    
        u += 1          

    if i % 2 != 0:       
        a.reverse()       
    if i == 0:
        print(*a, sep=2*' ') 
    else:
        print(*a)
