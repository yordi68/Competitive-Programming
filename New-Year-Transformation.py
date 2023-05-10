n , k = list(map(int, input().split()))
arr = list((map(int, input().split())))

idx = 1
while idx <= k:
    if idx == k:
        print("Yes")
        break
    idx = arr[idx - 1] + idx
else:
    print("NO")
