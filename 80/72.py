phi = [0]*int(1e6+10)
for i in range(len(phi)):
    phi[i] = i-1
for i in range(2,len(phi)):
        for j in range(i*2,len(phi),i):
            phi[j] -= phi[i]
            
            
f = [0,2]
for i in range(2,int(1e6+1)):
    f.append(f[-1]+phi[i])
print(f[8])
print(f[-1]-2)