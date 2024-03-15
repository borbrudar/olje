p = [1] * int(1e6+10)
pp = []
p[1]=0
for i in range(2,len(p)):
    if p[i] == 0: continue 
    if len(pp) > 1000: break
    pp.append(i)    
    for j in range(i*2,len(p),i): p[j] = 0 


can = [0]*int(50_000_000)
print(pp[-1])
for i in range(len(pp)):
    for j in range(len(pp)):
        for k in range(len(pp)):
            val = pp[i]**2 + pp[j]**3 + pp[k]**4
            if val >= 50_000_000:break
            can[val]=1
            
print(sum(i==1 for i in can))