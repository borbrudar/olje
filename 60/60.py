p = [1] * int(1e9+10)
p[1]=0
st= set()
vec=[]
for i in range(2,len(p)):
    if p[i] == 0: continue    
    if len(vec) <= 10000: vec.append(i)
    st.add(i)
    for j in range(i*2,len(p),i): p[j] = 0

ans=100000000000000000000

for a in range(0,len(vec)):
    for b in range(a+1,len(vec)):
        if int(str(vec[a]) +str(vec[b])) not in st or int(str(vec[b]) +str(vec[a])) not in st: continue
        for c in range(b+1,len(vec)):
            if int(str(vec[a]) +str(vec[c])) not in st or int(str(vec[c]) +str(vec[a])) not in st: continue
            if int(str(vec[b]) +str(vec[c])) not in st or int(str(vec[c]) +str(vec[b])) not in st: continue
            for d in range(c+1,len(vec)):
                if int(str(vec[a]) +str(vec[d])) not in st or int(str(vec[d]) +str(vec[a])) not in st: continue
                if int(str(vec[b]) +str(vec[d])) not in st or int(str(vec[d]) +str(vec[b])) not in st: continue
                if int(str(vec[c]) +str(vec[d])) not in st or int(str(vec[d]) +str(vec[c])) not in st: continue
                for e in range(d+1,len(vec)):
                    if int(str(vec[a]) +str(vec[e])) not in st or int(str(vec[e]) +str(vec[a])) not in st: continue
                    if int(str(vec[b]) +str(vec[e])) not in st or int(str(vec[e]) +str(vec[b])) not in st: continue
                    if int(str(vec[c]) +str(vec[e])) not in st or int(str(vec[e]) +str(vec[c])) not in st: continue
                    if int(str(vec[d]) +str(vec[e])) not in st or int(str(vec[e]) +str(vec[d])) not in st: continue
                    ans=min(ans,vec[a]+vec[b]+vec[c]+vec[d]+vec[e])

print(ans)
