class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        _max = max(arr)
        answer = []
        
        for i in range(n):
            if i == n - 1:
                answer.append(-1)
                return answer
            if arr[i] == _max:
                temp = arr[n - 1:i:-1]
                _max = max(temp)
                
                
            answer.append(_max)
            
    