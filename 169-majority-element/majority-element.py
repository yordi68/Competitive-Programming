class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for i in range(len(nums)):
            count[nums[i]] += 1
        
        return max(count, key=count.get)