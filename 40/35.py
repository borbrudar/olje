p = [1] * int(1e7+10)


for i in range(2,len(p)):
    if p[i] == 0: continue 
    for j in range(i*2,len(p),i): p[j] = 0
    
cnt = 0
for i in range(2,len(p)):
    if p[i] == 0: continue
    s = str(i)
    if len(s)==1: 
        cnt+=1
        continue 
    ok=1
    for j in range(1,len(s)):
        a = int(s[j:len(s)] + s[0:j])
        if p[a] == 0: ok = 0
    if ok == 1: cnt+=1
    
    
print(cnt)