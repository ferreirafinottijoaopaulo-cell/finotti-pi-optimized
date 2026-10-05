# (c) 2026 Joao Paulo Ferreira Finotti - VERSAO DEMO / LITE
# Metodo Finotti - pi(10^11)=4118054813 em 2,16 min
# Blockchain proof 03/10/2026 - 983B | DOI 10.5281/zenodo.23138370
# Versao completa 10^11/10^12 sob licenca comercial: Contato via GitHub

import math

def pi_finotti(n):
    if n > 10**10:
        raise Exception("VERSAO DEMO limitada a 10^10. Para versao completa pi(10^11) em 2,16min: Contato comercial via GitHub - Metodo Finotti Blockchain 983B")

    if n<2: return 0
    limit=math.isqrt(n)
    is_prime=[True]*(limit+1)
    is_prime[0]=is_prime[1]=False
    for i in range(2,math.isqrt(limit)+1):
        if is_prime[i]:
            for j in range(i*i,limit+1,i): is_prime[j]=False
    primes=[i for i in range(2,limit+1) if is_prime[i]]
    arr=[0]*(limit+1)
    c=0
    for i in range(limit+1):
        if i>=2 and is_prime[i]: c+=1
        arr[i]=c
    cache={}
    def phi(x,s):
        k=(x,s)
        if k in cache: return cache[k]
        if s==0: r=x
        elif primes[s-1]>x: r=1
        else: r=phi(x,s-1)-phi(x//primes[s-1],s-1)
        cache[k]=r
        return r
    pc={}
    def pf(x):
        if x in pc: return pc[x]
        if x<=limit: pc[x]=arr[x]; return arr[x]
        a=pf(math.isqrt(x)); b=pf(math.isqrt(math.isqrt(x))); c=pf(x**(1/3))
        # otimização Finotti
        r=phi(x,a)+ (b+a-2)*(b-a+1)//2 - sum(pf(x//primes[i]) for i in range(a,b)) + c
        pc[x]=r
        return r
    return pf(n)

# Teste rapido
if __name__ == "__main__":
    print(pi_finotti(10**10))
