n, x = map(int, input().split())
s = 0                    
for i in range(1,n+1):   
    for j in range(1,n+1):
        if i*j==x:        
            s+=1           
print(s)