from collections import defaultdict

def build_sieve(num):
    sieve = [0 for i in range(num + 1)]
    
    for i in range(num + 1):
        sieve[i] = i
    
    i = 2
    
    while i * i <= num:
        if sieve[i] == i:
            for j in range(i * i, num + 1, i):
                if (sieve[j] == j):
                    sieve[j] = i
        i += 1

    return sieve

def prime_factorization(num, sieve):
    factors = defaultdict(int)
    d = 2

    while num > 1:
        sf = sieve[num]
        factors[sf] += 1
        num //= sf

    return factors 

def main():
    length, power = map(int, input().split())
    nums = list(map(int, input().split()))
    multiplicand = defaultdict(int)
    sieve = build_sieve(100_000)
    ans = 0

    for num in nums:
        prime_factors = prime_factorization(num, sieve)
        multiplier = 1

        for factor in prime_factors:
            exponent = prime_factors[factor]
            modulo = exponent % power

            if modulo != 0:
                multiplier *= (factor ** (power - modulo))
            
        
        ans += multiplicand[multiplier]
        cur_multiplicand = 1
        
        for factor in prime_factors:
            exponent = prime_factors[factor]
            modulo = exponent % power
            cur_multiplicand *= (factor ** modulo)
            
        multiplicand[cur_multiplicand] += 1
    
    print(ans)

main()