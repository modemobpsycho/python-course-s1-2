nums = list(map(int, input().split()))

valid_nums = []
for i in nums:
    if i > 0:
        valid_nums.append(i)

if len(valid_nums) == 0:
    print('Empty')
else:
    print(min(valid_nums))
