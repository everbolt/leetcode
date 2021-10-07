from functools import lru_cache

from math import isqrt

def A010815(n):
    m = isqrt(24*n+1)
    return 0 if m**2 != 24*n+1 else ((-1)**((m-1)//6) if m % 6 == 1 else (-1)**((m+1)//6)) # Chai Wah Wu, Sep 08 2021

@lru_cache(maxsize=None)
def steper(n): return 1 if n == 0 else A010815(n)+2*sum((-1)**(k+1)*steper(n-k**2) for k in range(1, isqrt(n)+1)) # Chai Wah Wu, Sep 08 2021

step = lambda x: steper(x) - 1