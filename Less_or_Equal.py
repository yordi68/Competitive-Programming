n , k = list(map(int,input().split()))
a = list(map(int,input().split()))
a.sort()
if k == 0:
    if a[0] > 1:
        print(1)
    else:
        print(-1)
elif n == k:
    print(a[n - 1])
elif a[k - 1] == a[k]:
    print(-1)
else:
    print(a[k - 1])
