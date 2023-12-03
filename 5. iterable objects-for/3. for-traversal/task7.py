numbers = list(map(int, input().split()))
r = int(input())
found_index = -1
for i in range(len(numbers)):
    if numbers[i] == r:
        found_index = i + 1
        break
if found_index != -1:
    print(found_index)
else:
    print("ErrorValue")
