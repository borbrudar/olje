from math import isqrt
def isPrime(n):
    if n <= 0: return 0
    for i in range(2,isqrt(n)+1):
        if n%i==0: return 0
    return 1

mx = 0
ans=0
for a in range(-1000,1001):
    for b in range(-1000,1001):
        n=0
        while isPrime(n*n + n*a + b) == 1: n+=1
        if n > mx: 
            mx = n 
            ans = b*a
print(ans)   