from collections import deque

def is_valid_cell(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def has_cycle(grid, n, m):
    # directions to move in the grid
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # visited set to track visited cells
    visited = set()

    # perform bfs from each cell
    for i in range(n):
        for j in range(m):
            if (i, j) in visited:
                continue

            color = grid[i][j]
            q = deque([(i, j, None)])

            while q:
                x, y, prev = q.popleft()
                if (x, y) in visited:
                    # cycle found
                    return True

                visited.add((x, y))

                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]

                    if not is_valid_cell(nx, ny, n, m) or grid[nx][ny] != color:
                        continue

                    if (nx, ny) != prev:
                        q.append((nx, ny, (x, y)))

    # no cycle found
    return False

# read input
n, m = map(int, input().split())
grid = [input() for _ in range(n)]

# check if there is a cycle
if has_cycle(grid, n, m):
    print("Yes")
else:
    print("No")