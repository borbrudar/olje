p = [1] * int(1e6+10)
pp = list()
st = set()
p[1]=0
for i in range(2,len(p)):
    if p[i] == 0: continue 
    pp.append(i)
    st.add(i)
    for j in range(i*2,len(p),i): p[j] = 0
    

ans =0
mx=0
for i in range(len(pp)):
    cur = 0
    for j in range(i,len(pp)):
        cur+=pp[j]   
        if cur > 1_000_000: break 
        if cur in st: 
            if mx < j-i+1:
                mx= j-i+1
                ans=cur
        
print(ans)