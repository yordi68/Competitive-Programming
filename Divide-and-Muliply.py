n = int(input())
for _ in range(n):
    n = int(input())
    arr = list(map(int , input().split()))
    div = 1

    for i in range(len(arr)):
        while arr[i] % 2 == 0:
            arr[i] //= 2
            div *= 2
    arr.sort()
    div = arr[-1] * div
    arr.pop()
    div += sum(arr)
    print(div)
    