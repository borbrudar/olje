p = [1] * int(1e6+10)

p[1]=0
for i in range(2,len(p)):
    if p[i] == 0: continue 
    for j in range(i*2,len(p),i): p[j] = 0
    
ans=0
for i in range(10,len(p)):
    if p[i] == 0 : continue
    ok = 1
    n=i
    while n > 0:
        if p[n] == 0: ok=0
        n//=10        
    n=str(i)
    while len(n) > 0:
        if p[int(n)] == 0: ok =0
        n = n[1:len(n)]
    if ok==1: ans+=i
print(ans)