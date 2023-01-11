class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        for sentence in sentences:
            counter = 0
            for chx in sentence:
                if chx == " ":
                    counter += 1
                
            count = max(count,counter)
            
        return count + 1
                