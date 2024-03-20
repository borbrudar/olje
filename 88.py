# lhk gredas prastevilski razcep od N
# pa dodajas zdruzujes u iste potence vsota je zmeri ista
# sestejes prafaktorje in ce je mansi od N lhk se dodajas nekej 1nk
# prastevila nimajo veze
# tk da lhk sm zracunas min k za neko stevilo (ce so usi prafaktorji skup)
# t.j. stevilo prafaktorjev 
# pa max ki je ce so usi skup pa pol enke
# pol pa updatas ta range in mas resitev
# e.g. 8 = 2 * 2 * 2 vsota je 6, dodas 2 enke k = 2 + 3 = 5
# ce je stevilo enk > 0 potem je min k enak 2
# ce ne je st enk + 1 
# 9 = 3*3 vsota je 6, 3 enke, k =2+3 = 5 oz 3 + 1 = 4, 8mke ze zafilajo

# ok ne k druge faktorji majo druge vsote....bi mogu nekak prevert use mozne kombinacije....
from math import isqrt
mn = [10000000000]*12001
n=int(1000)
spf = [1]*n
for i in range(n):spf[i]=i
for i in range(2,n):
    for j in range(i*2,n,i):
        spf[j] = i


for i in range(4,n):
    if i%10000==0: print(i)
    sm = 0
    cnt =0 
    cur = i
    minf = 0
    maxf = 0
    while cur != 1:
        fact = cur//spf[cur]
        maxf = max(maxf,fact)
        minf = min(minf,fact)
        if spf[cur] == cur:
            maxf = max(maxf,cur)
            minf = min(minf,cur)
            sm+=cur
            cnt+=1
            break
        if fact == 1: break
        sm += fact
        cnt+=1
        cur = spf[cur]        
     
    if cnt == 0 or sm > i: continue # prastevilo al pa slabo
    enk = i-sm
    maxk = min(12000,enk + cnt)
    mink = max(2,enk+2)
    
    ip = mink
    while ip<=maxk:
        mn[ip] =min(mn[ip],i)
        ip+=1
    
st = set()
for i in range(2,13):
    if mn[i] == 10000000000:i//=0
        #print(i)
    st.add(mn[i])
ans=0
for i in st:ans+=i
print(ans)