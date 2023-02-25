length = int(input())

neg_cnt = 0
zero_cnt = 0
ans = 0

nums = list(map(int, input().split()))

for i in range(length):
    if nums[i] == 0:
        ans += 1
        zero_cnt += 1
    elif nums[i] < 0:
        ans += (-1 - nums[i])
        neg_cnt += 1
    else:
        ans += nums[i] - 1

if neg_cnt % 2 == 1 and zero_cnt == 0:
    ans += 2

print(ans)