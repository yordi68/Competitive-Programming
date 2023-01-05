class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        strlist = []
        n = len(spaces)
        for i in range(n):
            if i == 0:
                strlist.append(s[:spaces[i]] +" ")
            else:
                strlist.append(s[spaces[i - 1]:spaces[i]] +" ")
            if i == n - 1:
                strlist.append(s[spaces[i]:len(s)])
                
        return "".join(strlist)