class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        distance = float("inf")
        
        for i in range(n - 2):
            left = i + 1
            right = len(nums) - 1
            newtarget = target - nums[i]
            
            while left < right:
                total = nums[left] + nums[right]
                if abs(distance) > abs(newtarget - total):
                    distance = newtarget - total
                
                if total == newtarget:
                    return target
                elif total < newtarget:
                    left += 1
                else:
                    right -= 1
                    
        return target - distance