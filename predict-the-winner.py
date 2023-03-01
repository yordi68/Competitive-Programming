class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
    
        def fun(arr,l,r,t):

            if l == r:
                if t:
                    return [arr[l],0]
                else:
                    return [0,arr[l]]

            if t:
                right = fun(arr,l,r - 1,False)
                right[0] += arr[r]
                left = fun(arr,l + 1, r,False)
                left[0] += arr[l]
                if right[0] >= left[0]:
                    return right
                else:
                    return left

            else:
                right = fun(arr,l,r - 1,True)
                right[1] += arr[r]
                left = fun(arr,l + 1, r,True)
                left[1] += arr[l]
                if right[1] >= left[1]:
                    return right
                else:
                    return left

        ans = fun(nums,0,len(nums) - 1,True)
        return ans[0] >= ans[1]