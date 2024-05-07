class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [1] * n

    # Use ans as the prefix product array.
    for i in range(1, n):
      ans[i] = ans[i - 1] * nums[i - 1]

    suffix = 1  # suffix product
    for index, val in reversed(list(enumerate(nums))):
      ans[index] *= suffix
      suffix *= val


    return ans