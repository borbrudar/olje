from math import isqrt
n = int(1e6)
d = [0]*n

for i in range(1,n):
    for j in range(i*2,n,i):
        d[j] += i        
ans = 0
mx = 0

vis= [0]*n
for i in range(2,n):
    if vis[i] == 1: continue 
    vis[i]=1
    st = set()
    #st.add(i)
    cur = i
    bad=0
    while 1:
        cur = d[cur]
        if cur == 1:
            bad =1
            break
        if cur > n:
            bad=1
            break
        if cur in st:
            bad = 1
            break
        elif cur == i:
            break
        else : 
            st.add(cur)
    if bad==1:continue
    if len(st) > mx:
        for u in st: vis[u] = 1
        mx = len(st)
        ans = i
print(ans)