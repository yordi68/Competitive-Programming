class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        n = len(nums)

        for number in nums:
            hashmap[number] += 1
            if hashmap[number] > floor(n / 2):
                return number

        