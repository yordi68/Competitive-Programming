class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:

        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(sqrt(num))+1):
                if num % i == 0:
                    return False
            return True

        prime_factors = Counter()

        for num in nums:
            if is_prime(num):
                prime_factors[num] += 1
                continue
                
            for i in range(2, int(sqrt(num))+1):
                while num % i == 0:
                    prime_factors[i] += 1
                    num = num // i
                    
            if num > 1:
                prime_factors[num] += 1
                
        return len(prime_factors)