n, m = map(int, input().split()) 
a = [[str(j) for j in input()] for i in range(n)]  
count = 0                   
for i in range(n):          
    for j in range(m):       
        if a[i][j] != '*':    
            for d in (-1, 1):  
                ai = i + d    
                if 0 <= ai < n and a[ai][j] == '*':  
                    break     
                aj = j + d   
                if 0 <= aj < m and a[i][aj] == '*':  
                    break    
            else:
                count += 1     
print(count)