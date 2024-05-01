class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                temp = word[0: i + 1]
                temp = temp[::-1]
                temp += word[i + 1: len(word)]
                return temp
        return word
        
