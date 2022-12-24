class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(n):
            for j in range(len(arr))[::-1]:
                if i != j:
                    if arr[j] == arr[i] * 2:
                        return True
                    
        return False
            
            
                
                
                