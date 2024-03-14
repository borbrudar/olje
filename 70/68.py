from itertools import permutations
vec = [1,2,3,4,5,6,7,8,9,10]

ans = 0
for a_ in range(len(vec)):
    for b_ in range(a_+1,len(vec)):
        for c_ in range(b_+1,len(vec)):
            for d_ in range(c_+1,len(vec)):
                for e_ in range(d_+1,len(vec)):
                    a=vec[a_]
                    b=vec[b_]
                    c=vec[c_]
                    d=vec[d_]
                    e=vec[e_]
                    tmp = [a,b,c,d,e]
                    rem = []
                    for i in vec: 
                        if i!=a and i!=b and i!=c and i!=d and i!=e: rem.append(i)
    
                    for perm in list(permutations(tmp)):
                        for outer_perm in list(permutations(rem)):
                            if outer_perm[0] != min(rem): continue
                            s=str()
                            totals=[]
                            for i in range(5):
                                s += str(outer_perm[i]) + str(perm[i]) + str(perm[(i+1)%5])                            
                                totals.append(outer_perm[i] + perm[i] + perm[(i+1)%5])
                            if max(totals) != min(totals):continue
                            if len(s) ==16:
                                ans=max(ans,int(s))
                                #print(s)
                            
                    
print(ans)                    
# torej 10 choose 5 krat 5! pol pa zberes zmeri sm najvecjo resitev 