a = int(input()) - 1 
b = int(input())

while a < b:
    a += 1  
    if a % 777 == 0:
        break     
    if a % 2 == 0 or a % 3 == 0:
        continue 
    print(a)
