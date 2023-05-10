tt = int(input())
import heapq
while tt:
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    b = list(map(int, input().split()))

    heapq.heapify(arr)
    for num in b:
        heapq.heappop(arr)
        heapq.heappush(arr, num)

    print(sum(arr))
    tt -= 1
    

    

