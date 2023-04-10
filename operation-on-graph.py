vertex = int(input())
operation = int(input())
from collections import defaultdict
adjList = defaultdict(list)
for _ in range(operation):
    arr = list(map(int , input().split()))
    if arr[0] == 1:
        adjList[arr[1]].append(arr[2])
        adjList[arr[2]].append(arr[1])
    if arr[0] == 2:
        print(*(adjList[arr[1]]))