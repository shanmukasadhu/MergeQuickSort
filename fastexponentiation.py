# Fast Exponentiation:
# a^n % p

import math
def exponentiation(a,n,p):
    if(n <= 1):
        return (a**n) % p
    b = exponentiation(a, math.floor(n/2), p)
    if(n % 2 ==0):
        return (b**2) % p
    else:
        return ((b**2) * a) % p
    

a = 2
n = 100
p = 137

print(exponentiation(2,100,137))
    