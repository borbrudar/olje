p = [1] * int(1e5+10)
comps = [0] * int(1e5+10)
p[1]=0

for i in range(2,len(p)):
    if p[i] == 0: continue
    k=1
    while i + 2*k**2 < len(comps):
        comps[i + 2* k**2]=1
        k+=1
    for j in range(i*2,len(p),i): p[j] = 0
    
for i in range(2,len(comps)):
    if p[i] == 1 or i%2==0: continue
    if comps[i] == 0: 
        print(i)
        break