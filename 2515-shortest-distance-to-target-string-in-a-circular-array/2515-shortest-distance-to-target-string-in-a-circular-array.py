class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        
        def left(i):
            count = 0
            while words[i] != target:
                count += 1
                i -= 1
                if i == -1:
                    i = n - 1
            return count
        def right(i):
            count = 0
            while words[i] != target:
                count += 1
                i += 1
                if i == n:
                    i = 0
            return count

        for word in words:
            if word == target:
                return min(left(startIndex),right(startIndex))
            
        return -1