class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = r = res = 0
        hashmap = {}
        while r < len(fruits):
            hashmap[fruits[r]] = r
            if len(hashmap) > 2:
                drop = min(hashmap.values())
                del hashmap[fruits[drop]]
                l = drop + 1
            res = max(res,r - l + 1)
            r += 1
        return res