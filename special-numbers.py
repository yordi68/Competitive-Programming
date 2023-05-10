t = int(input())
for i in range(t):
    n , k =  list(map(int , input().split()))
    total = 0
    i = 0
    while k:
        if k & 1 == 1:
            total += n ** i
        i += 1
        k >>= 1
    print(total % (10 ** 9 + 7))
    
