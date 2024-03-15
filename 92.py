n = int(1e7+1)
ed = [0]*n

def nxt(n):
    cur = 0
    while n>0:
        cur += (n%10)**2
        n//=10
    return cur

ed[1] = 1
ed[89] = 89
for i in range(1,n):
    if i%100000==0: print(i)
    if ed[i] != 0: continue
    st = set()
    st.add(i)
    cend = 0
    cur=i
    while 1:
        cur = nxt(cur)
        if ed[cur] != 0:
            cend = ed[cur]
            break
        else: st.add(cur)
    for u in st: ed[u]=cend
    
print(sum(i == 89 for i in ed))