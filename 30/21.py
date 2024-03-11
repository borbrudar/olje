from math import isqrt

def d(n):
    cnt = 1
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            if i*i == n: cnt+=i 
            else : cnt += i+n//i 
    return cnt

ans=0

for i in range(1,10001):
    if i == d(d(i)) and d(i) != i: ans+=i
print(ans)