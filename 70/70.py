phi = [0]*int(1e7+1)
for i in range(len(phi)):
    phi[i] = i
for i in range(2,len(phi)):
    if phi[i]==i:
        for j in range(i*2,len(phi),i):
            phi[j] -= phi[j]//i

            
mn = 100000000000000000000
ans = 0
for i in range(2,len(phi)):
    if phi[i] == i: continue
    s = list(str(i))
    s2 = list(str(phi[i]))
    s.sort()
    s2.sort()
    if s != s2: continue 
    if i/phi[i] < mn:
        mn = i/phi[i]
        ans=i    

print(ans)