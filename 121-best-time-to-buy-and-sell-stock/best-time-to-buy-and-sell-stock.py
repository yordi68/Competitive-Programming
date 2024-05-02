class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        maxDiff = 5
            | 1,  
            if incoming > there => subrtract them and give the value to maxDiff
            if incoming < there => pop out of the stack
            | 1, 
        
        """

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
