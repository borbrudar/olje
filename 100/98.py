with open("98.in") as f:
    vec = f.read().replace(","," ").replace("\"","").split(" ")

#print(max(len(vec[i]) for i in vec))
    
def isSame(s1,n1,s2,n2):
    # n1 pa n2 sta si ista, mors sm prevert da s1==n1 in s2==n2 za isto pravilo
    if len(s1) != len(n1): return 0
    ok=1
    rules = {}
    vis = [0]*len(s1)
    s1 = list(s1)
    used = []
    for i in range(len(s1)):
        if vis[i] == 1: continue
        if n1[i] in used: return 0
        
        rules[s1[i]] = n1[i]
        used.append(n1[i])
        rep = s1[i]
        for j in range(i,len(s1)):
            if s1[j] != rep: continue
            vis[j]=1 
            s1[j]=n1[i]
    if "".join(s1) != n1: return 0        
    
    s2=list(s2)
    for i in range(len(s2)):
        if s2[i] not in rules: return 0
        s2[i] = rules[s2[i]]
    if "".join(s2) != n2: return 0
    
    return 1
    
perms = {}

for i in range(int(1e4)):
    l = list(str(i*i))
    l.sort()
    s="".join(l)
    if s not in perms:
        perms[s]=[]
    perms[s].append(str(i*i))

       
ans = 0
for i in vec:
    l1 = list(i)
    l1.sort()
    for j in vec:
        if i ==j:continue
        l2 = list(j)
        l2.sort()
        if l1 != l2: continue
        # najdu permutacijo
        for pp in perms:
            if len(pp) == 1:continue
            for u in perms[pp]:
                for v in perms[pp]:
                    if u==v:continue
                    # najds dva in prevers ce je actually actually ista permutacija
                    if isSame(i,u,j,v)==1: 
                        ans=max(ans,int(u))
                        ans=max(ans,int(v))            
print(ans)

#print(to_standard_string("9126"))

# CARE ---> ABCD <--- 9216
# map<vector<>, vector<>>
# // elementi permutacije (sortiran list), vrednost kvadrata
# actually lhk kvadrate slikas u ta map
# pa podobnu za string, pa sm prevers da sta usaj 2 stringa not
# uu map<vector<>,int> je tut ok sm najvecjo hrans
# actually ne k morta bit obe v paru kvadrata....
# in mora bit tocn tista permutacija grrr
# ok kr je tuk mau permutacij lhk grez cez use in pol usakic cez ceu perms array da najdes matche :skull: