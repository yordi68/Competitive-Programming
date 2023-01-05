class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        count = 0
        
        for num in nums:
            tmp = num + k
            tmp2 = num - k
            if tmp in seen:
                count += seen[tmp]
            if tmp2 in seen:
                count += seen[tmp2]
                
            seen[num] += 1
        
        return count