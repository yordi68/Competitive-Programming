class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.ans = []
        
        
        def findCombinations(idx, candidates, target, ds):
            if idx == len(candidates):
                if target == 0:
                    self.ans.append(ds)
                return
            
            
            if candidates[idx] <= target:
                ds.append(candidates[idx])
                findCombinations(idx, candidates, target - candidates[idx], ds[:])
                ds.pop()
                
            findCombinations(idx + 1, candidates, target, ds[:])
            
            
        findCombinations(0, candidates, target, [])
        
        return self.ans