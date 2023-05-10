n = int(input())
arr = list(map(int , input().split()))

nums = [0]
for i in range(len(arr)):
    nums.append(arr[i])
temp = 0
for i in range(1 , n + 1):
        if nums[nums[nums[i]]] == i:
            temp = 1
            break

if temp == 1:
    print("YES")
else:
    print("NO")



