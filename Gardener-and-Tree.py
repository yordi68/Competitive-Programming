from collections import defaultdict
tt = int(input())
while tt:
    input()
    n, k = list(map(int, input().split()))
    if n == 1:
        print(0)
        tt -= 1
        continue
    # print()
    degree = defaultdict(int)
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = list(map(int, input().split()))
        graph[v].append(u)
        graph[u].append(v)
        degree[v] += 1
        degree[u] += 1

        
    from collections import deque
    queue = deque()
    for node, count in degree.items():
        if count <= 1:
            queue.append(node)

    cnt = 0
    while queue and k:
        m = len(queue)

        for _ in range(m):
            curr = queue.popleft()
            cnt += 1
            for node in graph[curr]:
                degree[node] -= 1
                if degree[node] == 1:
                    queue.append(node)
        k -= 1
    print(n - cnt)
    tt -= 1

