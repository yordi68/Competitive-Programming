n, m, k = list(map(int,input().split()))
arr = []
for _ in range(m):
    arr.append(int(input()))
fedor = int(input())
pair = 0
for num in arr:
    xor = (num ^ fedor)
    
    if bin(xor).count('1') <= k:
        pair += 1
print(pair)