    n = int(input())
    arr = list(map(int,input().split()))
    l = 0
    r = 0
    res = 1
    for r in range(1,len(arr)):
        if arr[r] >= arr[r - 1]:
            res = max(res,r - l + 1)
        else:
            l = r
    print(res)