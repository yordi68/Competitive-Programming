n = int(input())
arr = list(map(int, input().split()))
count = 0
odd = []
 
for i in range(n-1):
    _min = i
    for j in range(n - 1,i,-1):
        if arr[j] < arr[_min]:
            _min = j
    if _min != i:
        count += 1
        arr[i] , arr[_min] = arr[_min] , arr[i]
        odd.append([i,_min])
 
print(count)
for k in range(len(odd)):
    print(*odd[k])