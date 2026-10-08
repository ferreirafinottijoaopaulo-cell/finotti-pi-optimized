# (c) 2026 Joao Paulo Ferreira Finotti - VERSAO DEMO / LITE
# Metodo Finotti - pi(10^11)=4118054813 | Blockchain 03/10/2026 983B
# DOI 10.5281/zenodo.23138370

import math, time
from functools import lru_cache

def pi_finotti(n):
    if n > 10**10:
        raise Exception("VERSAO DEMO limitada a 10^10. Full: contato via GitHub")
    if n < 2:
        return 0

    limit = math.isqrt(n)
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, math.isqrt(limit) + 1):
        if is_prime[i]:
            for j in range(i*i, limit+1, i):
                is_prime[j] = False

    primes = [i for i in range(2, limit+1) if is_prime[i]]
    pi_small = [0] * (limit + 1)
    c = 0
    for i in range(limit+1):
        if is_prime[i]:
            c += 1
        pi_small[i] = c

    @lru_cache(maxsize=None)
    def phi(x, s):
        if s == 0:
            return x
        if primes[s-1] > x:
            return 1
        return phi(x, s-1) - phi(x // primes[s-1], s-1)

    @lru_cache(maxsize=None)
    def pf(x):
        if x <= limit:
            return pi_small[x]

        # a = pi(x^1/4)
        a_root = math.isqrt(math.isqrt(x))
        a = pf(a_root)
        # b = pi(x^1/2)
        b_root = math.isqrt(x)
        b = pf(b_root)
        # c = pi(x^1/3) com correcao da raiz
        c_root = int(round(x ** (1/3)))
        while (c_root + 1) ** 3 <= x:
            c_root += 1
        while c_root ** 3 > x:
            c_root -= 1
        c3 = pf(c_root)

        r = phi(x, a) + (b + a - 2) * (b - a + 1) // 2
        for i in range(a + 1, b + 1):
            w = x // primes[i-1]
            r -= pf(w)
            if i <= c3:
                bi = pf(math.isqrt(w))
                for j in range(i, bi + 1):
                    r -= pf(w // primes[j-1]) - (j - 1)
        return r

    return pf(n)

if __name__ == "__main__":
    for test in [10**6, 10**7, 10**8]:
        t = time.time()
        try:
            v = pi_finotti(test)
            print(f"pi({test})={v} em {time.time()-t:.2f}s")
        except Exception as e:
            print(f"erro {test}: {e}")
