class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        return self.gcd(max(nums) , min(nums))
    def gcd(self , a , b):
        if b == 0:
            return a
        return self.gcd(b , a % b)