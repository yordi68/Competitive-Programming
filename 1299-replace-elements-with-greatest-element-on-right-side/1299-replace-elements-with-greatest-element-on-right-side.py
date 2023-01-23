class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        _max = -1
        
        for i in range(n - 1, - 1 ,-1):
            temp = arr[i]
            arr[i] = _max
            if temp > _max:
                _max = temp
        
        return arr
                
            
        

                
            
    