n , m = list(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
i = 0
j = 0
count = 0
ans = []

while i <= n - 1 and j <= m - 1:
    if arr1[i] < arr2[j]:
        i += 1
    else:
        ans.append(i)
        j += 1
while i <= n - 1:
    i += 1
while j <= m - 1:
    ans.append(i)
    j += 1
print(* ans)
