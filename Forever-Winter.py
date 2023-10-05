tt = int(input())
while tt:
    n, m = map(int, input().split())
    cnt = [0] * (n + 1)
    for i in range(m):
        u, v = map(int, input().split())
        cnt[u] += 1
        cnt[v] += 1

    _dict = {}
    for i in range(1, n + 1):
        if cnt[i] not in _dict:
            _dict[cnt[i]] = 1
        else:
            _dict[cnt[i]] += 1

    vertices = []
    for p in _dict:
        vertices.append(_dict[p])
    vertices.sort()
    
    if len(vertices) == 3:
        print(vertices[1], vertices[2] // vertices[1])
    else:
        print(vertices[0] - 1, vertices[1] // (vertices[0] - 1))


    tt -= 1


