class Solution:
    # def manhattan_distance(num1, num2, x, y):
    #     length = (abs(num1 - x) + abs(num2 - y))
    #     return length
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        
        minimum_distance = float("inf")
        minimum_distance_index = -1
        n = len(points)
        
        for i in range(n):
            num1,num2 = points[i]
            if num1 == x or num2 == y:
                length = (abs(num1 - x) + abs(num2 - y))
                if length < minimum_distance:
                    minimum_distance = length
                    minimum_distance_index = i

        return (minimum_distance_index)
    
