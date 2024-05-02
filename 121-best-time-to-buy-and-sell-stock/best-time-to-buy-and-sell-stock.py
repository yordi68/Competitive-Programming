class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        stack = []
        maxDiff = 0
        stack.append(prices[0])


        for price in prices:
            if price > stack[-1]:
                maxDiff = max(maxDiff, price - stack[-1])
            else:
                stack.pop()
                stack.append(price)

        return maxDiff
