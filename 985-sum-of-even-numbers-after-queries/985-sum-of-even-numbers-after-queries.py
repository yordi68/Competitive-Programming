class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answers = []
        nums_sum = 0
        for num in nums:
            if num % 2 == 0:
                nums_sum += num

        for query in queries:
            new_val = nums[query[1]] + query[0]
            if new_val % 2 == 0:
                if nums[query[1]] % 2 == 0:
                    nums_sum -= nums[query[1]]
                nums_sum += new_val
            elif new_val % 2 != 0 and nums[query[1]] % 2 == 0:
                nums_sum -= nums[query[1]]

            nums[query[1]] = new_val
            answers.append(nums_sum)

        return answers