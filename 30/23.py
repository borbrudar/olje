from math import isqrt

def isAb(n):
    cnt =1
    for i in range(2,isqrt(n)+1):
        if n%i!=0:continue
        if i*i == n: cnt += i
        else: cnt+= i + n//i    
    
    return cnt > n

vec = list()
for i in range(1,28124):
    if isAb(i): vec.append(i)

ok = [0]*28125

for i in range(len(vec)):
    for j in range(i,len(vec)):
        if vec[i]+vec[j] > 28123: continue
        ok[vec[i]+vec[j]]=1

cnt = 0
for i in range(1,28124):
    if ok[i] == 0: cnt+=i
print(cnt)