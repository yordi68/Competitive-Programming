n = int(input())
a = list(map(int,input().split()))
li = [0] * 2
l = 0
r = n - 1
count = 0
while l <= r:
    if count % 2 == 0:
        if a[l] > a[r]:
            li[0] += a[l]
            l += 1
        else:
            li[0] += a[r]
            r -= 1
    else:
        if a[l] > a[r]:
            li[1] += a[l]
            l += 1
        else:
            li[1] += a[r]
            r -= 1
    count += 1
 
print( * li)
