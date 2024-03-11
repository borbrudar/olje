pent = set()
for i in range(1,int(1e4)): pent.add(i*(3*i-1)//2)

d = 100000000000000000
for i in pent:
    for j in pent:
        if i <= j: continue 
        if i+j in pent and i-j in pent: d = min(d,i-j)        
print(d)
