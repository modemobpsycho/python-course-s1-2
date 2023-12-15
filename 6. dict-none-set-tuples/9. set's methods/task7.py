a = {int(i) for i in input().split()}
b = {int(i) for i in input().split()}

print(*sorted(a.difference(b)))
