class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        x, y = entrance
        queue = deque([(x, y)])
        visited = set((x, y))

        def inBound(row, col):
            return 0 <= row < len(maze) and 0 <= col < len(maze[0])

        level = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                if ((row == 0) or (col == 0) or (row == len(maze) - 1) or (col == len(maze[0]) - 1)):
                    if [row, col] != entrance:
                        return level

                for r, c in directions:
                    nr = r + row
                    nc = c + col
                    if inBound(nr, nc) and (nr, nc) not in visited and maze[nr][nc] == '.':
                        queue.append((nr, nc))
                        visited.add((nr, nc))

            level += 1


        return -1