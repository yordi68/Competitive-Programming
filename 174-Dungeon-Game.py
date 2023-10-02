class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    pass
                elif r == m - 1:
                    dungeon[r][c] += dungeon[r][c + 1]
                elif c == n - 1:
                    dungeon[r][c] += dungeon[r + 1][c]
                else:
                    dungeon[r][c] += max(dungeon[r + 1][c], dungeon[r][c + 1])

                dungeon[r][c] = min(0, dungeon[r][c])

        print(dungeon)
        return abs(dungeon[0][0]) + 1