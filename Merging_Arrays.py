n , m = list(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
i = 0
j = 0
res = []
while i <= n - 1 and j <= m - 1:
    if arr1[i] < arr2[j]:
        res.append(arr1[i])
        i += 1
    else:
        res.append(arr2[j])
        j += 1

while i <= n - 1:
    res.append(arr1[i])
    i += 1
while j <= m - 1:
    res.append(arr2[j])
    j += 1

print(* res)
