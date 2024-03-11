p = [1] * int(1e4+10)

p[1]=0
for i in range(2,len(p)):
    if p[i] == 0: continue 
    for j in range(i*2,len(p),i): p[j] = 0
    
    
for i in range(1000,10001):
    if p[i] == 0: continue
    for inc in range(1,10000):
        if i+2*inc >= 10000: break 
        j = i+inc
        k = i+2*inc 
        if p[j]==0 or p[k] ==0:continue 
        if set(str(i))==set(str(j)) and set(str(i))==set(str(k)):
            print(str(i)+str(j)+str(k))
