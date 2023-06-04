class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        self.memo = defaultdict(int)
        
        return self.dfs(amount) if self.dfs(amount) != float("inf") else -1
        
    def dfs(self, amount):
        left = float("inf")
        if amount== 0:
            self.memo[amount] = 0
            return self.memo[amount]
        
        if amount < 0:
            return float("inf")
        
        if amount in self.memo:
            return self.memo[amount]
    
        for coin in self.coins:
            left = min(left, self.dfs(amount - coin))
            
        self.memo[amount]= left + 1
        return self.memo[amount]  
            