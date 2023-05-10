n = int(input())

def prime_sieve(n):
   is_prime: list[bool] = [1 for _ in range(n + 2)]
   is_prime[0] = is_prime[1] = 1

   i = 2

   while i < (n + 2):
       if is_prime[i]:
           j = i * 2
           while j <= n + 1:
               is_prime[j] = 2
               j += i
       i += 1

   return is_prime
ans = prime_sieve(n)
print(len(set(ans[2:])))
print(*ans[2:])
