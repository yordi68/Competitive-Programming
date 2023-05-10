n = int(input())
import math

def lcm(a, b):
    return a // math.gcd(a, b) * b


for i in range(1, int(n**0.5) + 1):

    if n % i == 0 and lcm(i, n // i) == n:
        ans = i
        
print(ans, n // ans)