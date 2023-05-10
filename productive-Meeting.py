tt = int(input())

import heapq
while tt:
    size = int(input())
    arr = list(map(int, input().split()))
    ans = []
    maxHeap = []
    for i in range(len(arr)):
       heapq.heappush(maxHeap, [-arr[i], i+1]) 

    while len(maxHeap) > 1:
        num1, idx1 = (heapq.heappop(maxHeap))
        num2, idx2 = (heapq.heappop(maxHeap))
        num1 = -num1
        num2 = -num2
        if num1 and num2:
            num1 -= 1
            num2 -= 1
            ans.append([idx2, idx1])
            # print(["hi", idx2,idx1])
            
            if num1 > 0:
                heapq.heappush(maxHeap, [-num1, idx1])

            if num2 > 0:
                heapq.heappush(maxHeap, [-num2, idx2])

            

    print(len(ans))
    if ans:
        for e in ans:
            print(* e)
    tt -= 1