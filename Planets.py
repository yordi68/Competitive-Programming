tt = int(input())

while tt:
    n, c = list(map(int,input().split()))
    arr = list(map(int,input().split(" ")))
    cnt = 0

    from collections import Counter
    count = Counter(arr)

    for x in count:
        if count[x] == 1:
            cnt += 1
        elif count[x] < c:
            cnt += count[x]
        else:
            cnt += c
            
    print(cnt)
    tt -= 1