import math,time
def pi_finotti(n):
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
  a=pf(math.isqrt(math.isqrt(x)));b=pf(math.isqrt(x));c3=pf(int(x**(1/3)))
  r=phi(x,a)+(b+a-2)*(b-a+1)//2
  for i in range(a+1,b+1):
   w=x//primes[i-1];r-=pf(w)
   if i<=c3:
    bi=pf(math.isqrt(w))
    for j in range(i,bi+1): r-=pf(w//primes[j-1])-(j-1)
  pc[x]=r;return r
 return pf(n)
