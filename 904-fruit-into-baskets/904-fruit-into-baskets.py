class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,r,res = 0,0,0
        dic = {}
        while r < len(fruits):
            dic[fruits[r]] = r
            if len(dic) > 2:
                min_val = min(dic.values())
                del dic[fruits[min_val]]
                l = min_val + 1
            res = max(res,r - l + 1)
            r += 1
        return(res)