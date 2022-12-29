class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        #creating a dictionary that stores the elements in the deliciosness array        
        # with their frequency 
        ans = 0
        freq = {}
        
        for elm in deliciousness:
            for i in range(22):
                power = pow(2, i)
                if (power - elm) in freq:
                    ans += freq[power - elm]
            freq[elm] = freq.get(elm, 0) + 1
            
        return ans % (10 ** 9 + 7)