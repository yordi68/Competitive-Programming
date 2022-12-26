class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        length_words = len(words)
        
        for i in range(length_words):
            for j in range(i+1,length_words):
                count_element1 = set(words[i])
                count_element2 = set(words[j])
                if count_element1 == count_element2:
                    count += 1
                    
        return count