length = int(input())
nums = list(map(int, input().split()))

nums.sort()
ans = 0
left = 0
for right in range(length):
    while (nums[right] - nums[left]) > 5:
        left += 1
    
    ans = max(ans, right - left + 1)
    
print(ans)