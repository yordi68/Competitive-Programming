n = int(input())
for i in range(n):
    size , k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    count = 0
    temp = 0
    # l = 0
    r = 1
    while r < size:
        if (arr[r] * 2) > arr[r - 1]:
            temp += 1
        else:
            temp = 0
        if temp == k:
            count += 1
            temp -= 1
        r += 1
    print(count)
