class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        n1 = len(word1)
        n2 = len(word2)
        i = 0
        while i < n1 and i < n2:
            merged.append(word1[i])
            merged.append(word2[i])
            i += 1
        while i < n1:
            merged.append(word1[i])
            i += 1
        while i < n2:
            merged.append(word2[i])
            i += 1
        
        merged = "".join(merged)
        
        return merged