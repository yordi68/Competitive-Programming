t = int(input())
for _ in range(t):
    n , x = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    total = x * (1 + x) // 2
    
    for num in arr:
        if num <= x:
            total -= num * 2

    print(total)