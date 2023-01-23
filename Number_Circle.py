n = int(input())
arr = list(map(int,input().split()))
arr.sort()
if arr[-2] + arr[-3] > arr[-1]:
    arr[-1], arr[-2] = arr[-2] , arr[-1]
    print("YES")
    print(* arr)
else:
    print("NO")
