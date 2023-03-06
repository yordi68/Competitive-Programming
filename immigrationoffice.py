n = int(input())
arr = list(map(str,input().split()))
m = int(input())
for i in range(m):
    name = input()
    low = 0
    high = len(arr) - 1
    one = float("inf")
    while low <= high:
        mid = low + (high - low) // 2
        if name < arr[mid]:
            one = mid
            high = mid - 1
        elif name > arr[mid]:
            low = mid + 1
    print(one if one != float("inf") else len(arr))
        
    
    
