# (c) 2026 Joao Paulo Ferreira Finotti - VERSAO DEMO / LITE
# Metodo Finotti - pi(10^11)=4118054813 | Blockchain 03/10/2026 983B
# DOI 10.5281/zenodo.23138370
# Versao completa sob licenca: contato via GitHub

import math

def pi_finotti_demo(n):
    if n > 10**10:
        raise Exception("VERSAO DEMO limitada a 10^10. Full 10^11/10^12: contato comercial via GitHub")

    if n < 2: return 0
    limit = math.isqrt(n)
    is_prime = [True]*(limit+1)
    is_prime[0]=is_prime[1]=False
    for i in range(2, math.isqrt(limit)+1):
        if is_prime[i]:
            for j in range(i*i, limit+1, i):
                is_prime[j]=False

    primes = [i for i in range(2, limit+1) if is_prime[i]]
    pi_small = [0]*(limit+1)
    cnt=0
    for i in range(limit+1):
        if is_prime[i]: cnt+=1
        pi_small[i]=cnt

    from functools import lru_cache
    @lru_cache(None)
    def phi(x,s):
        if s==0: return x
        if primes[s-1] > x: return 1
        return phi(x,s-1) - phi(x//primes[s-1], s-1)

    @lru_cache(None)
    def pi_rec(x):
        if x <= limit: return pi_small[x]
        a = pi_rec(int(x**0.25))
        b = pi_rec(math.isqrt(x))
        c = pi_rec(int(round(x**(1/3))))
        res = phi(x,a) + (b+a-2)*(b-a+1)//2
        for i in range(a+1, b+1):
            w = x//primes[i-1]
            res -= pi_rec(w)
            if i <= c:
                bi = pi_rec(math.isqrt(w))
                for j in range(i, bi+1):
                    res -= pi_rec(w//primes[j-1]) - (j-1)
        return res
    return pi_rec(n)
