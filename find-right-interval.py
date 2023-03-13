class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        for i in range(len(intervals)):
            intervals[i].append(i)
        intervals.sort(key = lambda x : x[0])
        rightInterval = [-1] * len(intervals)

        for x , y , z in intervals:
            r = self.binarySearch( y , intervals)
            if r != -1:
                rightInterval[z] = r
            
        return rightInterval

    def binarySearch(self , value , intervals):
        left = 0
        right = len(intervals) - 1
        res = -1
        minStart = float("inf")
        while left <= right:
            mid = left + (right - left) // 2

            if intervals[mid][0] < value:
                left = mid + 1

            elif intervals[mid] [0] >= value:

                if intervals[mid][0] < minStart:
                    minStart = intervals[mid][0]
                    res = intervals[mid][2]
                right = mid - 1

        return res