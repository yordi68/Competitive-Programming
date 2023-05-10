arr = list(map(int , input().split()))
import math
gcd = []
val = math.gcd(arr[0] , arr[1])
for i in range(1,int(val**0.5) + 1):
    if val % i == 0:
        gcd.append(i)
        gcd.append(val // i)
gcd.sort()
n = int(input())
def binarySearch(ar,left , right):
    begin = -1
    end = len(ar) 
    while begin + 1 < end:
        mid = begin + (end - begin) // 2
        if ar[mid] <= right:
            begin = mid
        else:
            end = mid
    return begin
for _ in range(n):
    ar = list(map(int , input().split()))
    ans = binarySearch(gcd , ar[0] , ar[1])
    if ar[0] <= gcd[ans] <= ar[1]:
        print(gcd[ans])
    else:
        print(-1)




