n,m = map(int, input().split())
s = []                         
for i in range(n):
    s.append(input()) 
    
count_strok = 0         
count_stolb = 0           

for i in range(n):       
    if 'S' not in s[i]:   
        count_strok += 1   
        
for i in range(m):        
    s1 = []              
    for j in range(n):     
        s1.append(s[j][i]) 
        
    if 'S' not in s1:     
        count_stolb += 1   
         
print(count_strok * m + count_stolb * (n - count_strok))
