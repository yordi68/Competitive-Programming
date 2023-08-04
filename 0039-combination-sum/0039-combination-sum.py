class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        self.findCombinations(0, candidates, target, ans, [])
        
        return ans        
        
        
        
    def findCombinations(self, idx, arr, target, ans, carry):
        if idx == len(arr):
            if target == 0:
                ans.append(carry)   
            return
        
        if arr[idx] <= target:
            carry.append(arr[idx])
            self.findCombinations(idx, arr, target - arr[idx], ans, carry[:])
            carry.pop()
            
        self.findCombinations(idx + 1, arr, target, ans, carry[:])
        

