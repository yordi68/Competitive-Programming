class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        _dict = {}
        for i in range(n):
            _dict[s[i]] = i
            
        left = 0
        res = []
        last = 0
        for i in range(n):
            if _dict[s[i]] > last:
                last = _dict[s[i]]
            if i == last:
                res.append(last - left + 1)
                left = last + 1
                
        return res
                
                
            
            
            
            