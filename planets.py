from collections import Counter
n = int(input())
for i in range(n):
    m,p = list(map(int,input().split()))
    arr = list(map(int,input().split(" ")))
    arr = Counter(arr)
    total = 0
    for x in arr:
        if arr[x] == 1:
            total += 1
        elif arr[x] < p:
            total += arr[x]
        else:
            total += p
            
    print(total)
