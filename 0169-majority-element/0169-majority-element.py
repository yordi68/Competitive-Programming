class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1 
        hashmap = list(sorted(hashmap.items(),key=lambda x:x[1],reverse=True))
        return(hashmap[0][0])