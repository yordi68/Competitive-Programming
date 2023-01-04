class Solution:
    def closetTarget(self, words: List[str], target: str, s: int) -> int:

        if(target not in words):return -1
        else:
            c=1e9
            for i in range(0,len(words)):
                if(words[i]==target):
                    c=min(c,abs(i-s))
                    if(i>=s):c=min(c,s+len(words)-i)
                    else:
                        c=min(c,len(words)+i-s)
            return c