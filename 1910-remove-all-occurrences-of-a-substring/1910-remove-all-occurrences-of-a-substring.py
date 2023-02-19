class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        sub = []
        for char in s:
            sub.append(char)
            if len(sub) >= len(part):
                if ''.join(sub[len(sub) - len(part):]) == part:
                    sub[len(sub) - len(part):] = []
                    
        return ''.join(sub)