class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = []
        for num in range(left, right + 1):
            if num > 1 and self.isPrime(num):
                primes.append(num)
                if len(primes) >= 2 and primes[-1] - primes[-2] <= 2:
                    return [primes[-2], primes[-1]]
        
        if len(primes) > 1:
            ans = primes[:2]
            for i in range(len(primes) - 1):
                if ans[1] - ans[0] <= 2:
                    break
                if ans[1] - ans[0] > primes[i + 1] - primes[i]:
                    ans = [primes[i], primes[i + 1]]
            return ans
        else:
            return [-1, -1]

    def isPrime(self, num):
        d = 2
        while d * d <= num:
            if num % d == 0:
                return False 
            d += 1
        return True