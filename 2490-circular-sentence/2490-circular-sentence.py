class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        n = len(sentence)
        
        #check whether the first and the last character of the whole string are the same or not
        words = sentence.split()
        m = len(words)
        if sentence[0] != sentence[n - 1]:
            return False
        else:
            #iterating through the list and checking the fist chx and last chx are a  match
            for i in range(m-1):
                j = len(words[i]) - 1
                if words[i + 1][0] != words[i][j]:
                    return False
        
        return True