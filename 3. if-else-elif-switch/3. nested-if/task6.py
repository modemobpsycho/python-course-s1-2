a = input().lower()
b = input().lower()
if a != b:
    if a < b:
        print(-1)
    else:
        print(1)
else:
    print(0)
