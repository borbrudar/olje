with open("79.in") as f:
    vec = list(map(str,f.read().split("\n")))

g = []
for _ in range(11):g.append(set())
in_deg = [0]*10
out_deg = [0]*10


  
for i in vec:
    g[int(i[0])].add(int(i[1]))
    g[int(i[1])].add(int(i[2]))
    out_deg[int(i[0])]+=1
    in_deg[int(i[1])]+=1
    out_deg[int(i[1])]+=1
    in_deg[int(i[2])]+=1

vis = [0]*10

def dfs(v,p,ans):
    ans+=str(v)
    vis[v]+=1
    ok=1
    for i in range(10):
        if out_deg[i]==0 and in_deg[i]==0: continue
        if vis[i] == 0: ok=0        
    if out_deg[v] == 0 and ok==1:
        print(ans)
        exit()
    for i in g[v]:
        if i == p: continue
        dfs(i,v,ans)
    vis[v]-=1
        

#print(in_deg)
#print(out_deg)
for i in range(10):
    if in_deg[i] ==0 and out_deg[i] != 0: dfs(i,-1,"")