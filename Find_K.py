n = int(input())
for i in range(n):
    m,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    _dict = {}
    ans = "NO"
    for j in range(m):
        if arr[j] - k in _dict or arr[j] + k in _dict:
            ans = "YES"
            break
        _dict[arr[j]] = 1
 
    print(ans)
