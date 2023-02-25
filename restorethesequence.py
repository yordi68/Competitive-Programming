n = int(input())
for j in range(n):
    m = int(input())
    arr = list(map(int,input().split()))
    new = []
    l = 0
    r = m - 1
    if m % 2 == 0:
        while l < r:
            new.append(arr[l])
            new.append(arr[r])
            l += 1
            r -= 1
 
    else:
        while l <= r:
            new.append(arr[l])
            new.append(arr[r])
            l += 1
            r -= 1
        new.pop()
 
    print(* new)