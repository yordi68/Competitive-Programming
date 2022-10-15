class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       # [2,1]
    #[1,0,0,3,12]
        #l   r
       # [1,0,1]
          # l 
              #r
         #l r
            
        l=0
        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r]= nums[r],nums[l]
                l+=1