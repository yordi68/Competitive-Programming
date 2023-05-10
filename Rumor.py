n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
connected = []
for _ in range(m):
    connected.append(list(map(int, input().split())))

# building adjaceny list
from collections import defaultdict
adjList = defaultdict(list)
for x, y in connected:
    adjList[x].append(y)
    adjList[y].append(x)
# building the array with index and corresponding cost
for i in range(len(arr)):
    arr[i] = [i + 1, arr[i]]

#  sorting the array
sortedArr = sorted(arr, key = lambda x: x[1])


from collections import deque
visited = set()
def bfs(node):
    queue = deque()
    queue.append(node)

    while queue:
        curr = queue.popleft()

        for ele in adjList[curr]:
            if ele not in visited:
                queue.append(ele)
                visited.add(ele)

totalCost = 0
for idx,cost in sortedArr:
    if idx not in visited:
        totalCost += cost
        bfs(idx)

print(totalCost)

        

