phi = [0]*int(1e6+10)
for i in range(len(phi)):
    phi[i] = i
for i in range(2,len(phi)):
    if phi[i]==i:
        for j in range(i*2,len(phi),i):
            phi[j] -= phi[j]//i


mx=0
ans=0
for i in range(1,int(1e6+1)):
    if mx < i/phi[i]:
        mx=i/phi[i]
        ans=i
print(ans)