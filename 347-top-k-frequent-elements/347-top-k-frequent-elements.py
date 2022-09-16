
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        countnums = Counter(nums)
        a = countnums.most_common(k)
        ans = []
        for i in range(k):
            ans.append(a[i][0])
        return(ans)