class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        strlist = []
        pointer = 0
        for space in spaces:
            strlist.append(s[pointer:space] + " ")
            pointer = space
        strlist.append(s[pointer:len(s)])
                
        return "".join(strlist)