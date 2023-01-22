n = int(input())
for i in range(n):
    size = int(input())
    arr = list(map(int,input().split()))
    res = "YES"
    arr.sort()
    for i in range(size - 1):
        if arr[i + 1] - arr[i] > 1:
            res = "NO"
            break
    print(res)
