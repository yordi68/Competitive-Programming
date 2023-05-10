t = int(input())
import collections
def getLast(n):
    c = 0
    while n:
        n >>= 1
        c += 1
    return c
for i in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    
    d = collections.defaultdict(int)
    cnt = 0
    for num in arr:
        val = getLast(num)
        if val in d:
            cnt += d[val]
        d[val] += 1
    print(cnt)