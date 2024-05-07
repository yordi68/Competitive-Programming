class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_array = s.split(" ")

        for i in range(len(s_array) - 1, -1, -1):
            if s_array[i] != "":
                return len(s_array[i])
        
