from collections import defaultdict

def II():return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def MS(): return map(str,input().split())

def dfs(graph, node, color):
    stack = [node]
    while stack:
        node = stack.pop()
        new_color = 0 if color[node - 1] == 1 else 1
        for adj in graph[node]: 
            if color[adj - 1] != -1:
                if color[adj - 1] != new_color:
                    return False
            else:
                color[adj - 1] = new_color
                stack.append(adj)
    return True

V, E = MI()
edges = []
graph = defaultdict(list)
color = [-1] * V

for _ in range(E):
    u, v = MI()
    edges.append((u, v))
    graph[u].append(v)
    graph[v].append(u)
color[0] = 0
if dfs(graph, 1, color):
    print("YES")
    for u, v in edges:
        print(color[u - 1], end="")
else:
    print("NO")