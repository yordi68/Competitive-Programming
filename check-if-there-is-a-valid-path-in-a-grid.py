class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rep = {(i, j): (i, j) for i in range(len(grid)) for j in range(len(grid[0]))}
        size = {(i, j): 1 for i in range(len(grid)) for j in range(len(grid[0]))}

        direction = {
            1: [(0, 1), (0, -1)],
            2: [(1, 0), (-1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(-1, 0), (0, -1)],
            6: [(-1, 0), (0, 1)]
        }

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def find(x):
            if x != rep[x]:
                rep[x] = find(rep[x])
            return rep[x]

        def union(x, y):
            repx = find(x)
            repy = find(y)
            if repx != repy:
                if size[repx] > size[repy]:
                    rep[repy] = repx
                    size[repx] += size[repy]
                else:
                    rep[repx] = repy
                    size[repy] += size[repx]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for x, y in direction[grid[i][j]]:
                    row = i + x
                    col = j + y
                    if inbound(row, col):
                        for s, r in direction[grid[row][col]]:
                            nrow = row + s
                            ncol = col + r
                            if (nrow, ncol) == (i, j):
                                union((i, j), (row, col))

        return find((0, 0)) == find((len(grid) - 1, len(grid[0]) - 1))