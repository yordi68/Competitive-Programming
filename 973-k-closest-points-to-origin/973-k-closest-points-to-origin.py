class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
       import math
       a = []
       for i in range(len(points)):
           d = int(math.pow(points[i][0],2) + math.pow(points[i][1],2))
           a.append([d,points[i][0],points[i][1]])
       first =lambda x: x[0]
       a.sort(key=first)
       b = []
       for i in range(k):
           b.append([a[i][1],a[i][2]])
       return(b)



