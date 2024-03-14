from math import isqrt
n=int(1e5)


p = [0]*n
p[0] = 1
p[1] = 1
p[2] = 2

for i in range(3,n):
    for k in range(1,isqrt(i)+1):
        m = pow(-1,k-1)
        left = 0
        right = 0
        if i - k*(3*k+1)//2 >= 0: left = p[i - k*(3*k+1)//2] 
        if i - k*(3*k-1)//2 >= 0: right = p[i - k*(3*k-1)//2]
        p[i] += m*(left+right)
    if p[i]%1_000_000==0 and p[i]!=0:
        print(i)
        exit()
    