class Solution:
    def knightDialer(self, n: int) -> int:

        grid = [ [1, 2, 3],[4, 5, 6],[7, 8, 9],['*', 0, '#']]
        directions = [(2, 1), (-2, 1), (1, -2), (1, 2), (-2, -1), (-1, 2), (-1, -2), (2, -1)]

        def inBound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        @cache
        def dfs(i, j, rm):
            if rm == 0:
                return 1
            cnt = 0

            for r, c in directions:
                nr = r + i
                nc = c + j

                if inBound(nr, nc) and grid[nr][nc] != '*' and grid[nr][nc] != '#':
                    cnt += dfs(nr, nc,  rm - 1)

            return cnt

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '*' and grid[i][j] != '#':
                    ans += dfs(i, j, n - 1)
        print(ans)
        return ans % ((10 ** 9) + 7)
