from collections import defaultdict
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
adjList = defaultdict(list)
for r in range(len(arr)):
    for c in range(len(arr[0])):
        if arr[r][c] == 1:
            adjList[r].append(c)
            arr[c][r] = 0
roads = 0
for value in adjList.values():
    roads += len(value)

print(roads)