class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        len_word1 = len(word1)
        len_word2 = len(word2)
        merge = []
        while left < len_word1 and right < len_word2:
            if word1[left] != word2[right]:
                if ord(word1[left]) > ord(word2[right]):
                    merge.append(word1[left])
                    left += 1
                else:
                    merge.append(word2[right])
                    right += 1
            elif word1[left] == word2[right]:
                i = left
                j = right
                while i < len_word1 and j < len_word2 and word1[i] == word2[j]:
                    i += 1
                    j += 1
                if i == len_word1:
                    merge.append(word2[right])
                    right += 1
                elif j == len_word2:
                    merge.append(word1[left])
                    left += 1
                elif ord(word1[i]) > ord(word2[j]):
                    merge.append(word1[left])
                    left += 1
                else:
                    merge.append(word2[right])
                    right += 1
        
        while left < len_word1:
            merge.append(word1[left])
            left += 1
        while right < len_word2:
            merge.append(word2[right])
            right += 1
            
        return ''.join(merge)
            
    
                