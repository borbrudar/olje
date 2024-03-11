import math
ans = 0
n = 600851475143

for i in  range(2,math.isqrt(n)+1):
    while n%i == 0:
        ans=max(ans,i)
        n//=i
print(ans)