n=int(100)
from math import isqrt
p = [1] * n

p[1]=0
for i in range(2,len(p)):
    if p[i] == 0: continue 
    for j in range(i*2,len(p),i): p[j] = 0
    

k = [0]*n
sigma = [0]*n

sigma[1] =1
k[1] = 0

for i in range(2,n):
    for j in range(1,isqrt(i)+1):
        if i%j==0:
            if j*j == i:
                if p[j]==1: sigma[i]+=j
            else: 
                if p[j]==1:sigma[i]+=j
                if p[i//j]==1:sigma[i]+=i//j

for i in range(2,n):
    for j in range(1,i):
        k[i] += sigma[j]*k[i-j]
    k[i]+=sigma[i]
    k[i]//=i
    if k[i] > 5000:
        print(i+1)
        break
