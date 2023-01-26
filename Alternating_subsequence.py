n = int(input())
for i in range(n):
    m = int(input())
    a = list(map(int,input().split()))
    r = 0
    # _max = float("-inf")
    res = []

    while r < m:
        _max = a[r]
        while r + 1 < m and a[r] < 0 and a[r + 1] < 0:
            if a[r + 1] > _max:
                _max = a[r + 1]
            r += 1
        while r + 1 < m and a[r] > 0 and a[r + 1] > 0:
            if a[r + 1] > _max:
                _max = a[r + 1]
            r += 1
        r += 1
        res.append(_max)
    print(sum(res))
