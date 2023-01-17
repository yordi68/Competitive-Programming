class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for i in range(n):
            max = i
            for j in range(i + 1,n):
                if heights[j] > heights[max]:
                    max = j
                    
            heights[i] , heights[max] = heights[max] , heights[i]
            names[i] ,  names[max] = names[max] ,  names[i]

                    
                    
        return names
                    
                