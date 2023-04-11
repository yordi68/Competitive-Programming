class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, 1),(0, -1) , (1, 0),(-1, 0)]
        visited = set()
        change = image[sr][sc]
        image[sr][sc] = color
        def inBound(row , col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])

        def dfs(row , col):
            image[row][col] = color
            visited.add((row, col))
            for r , c in directions:
                newrow = row + r
                newcol = col + c

                if inBound(newrow , newcol) and (newrow , newcol) not in visited and image[newrow][newcol] == change:
                    dfs(newrow , newcol)


        dfs(sr , sc)
        return image