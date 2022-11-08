class Solution:
    def minimumSum(self, num: int) -> int:
        res = []
        num_list = list(str(num))
        l,r = 0,len(num_list) - 1
        num_list.sort()
        while l <= r:
            res.append(num_list[l] + num_list[r])
            l ,r = l + 1 , r - 1
        sum = int(res[0]) + int(res[1])
        return sum
         