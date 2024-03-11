pent = set()
for i in range(1,int(1e6)): pent.add(i*(3*i-1)//2)
triangles = list()
for i in range(1,int(1e6)):
    triangles.append(i*(i+1)//2)
hx = set()
for i in range(1,int(1e6)):
    hx.add(i*(2*i-1))
    
i = 286
while 1:
    if triangles[i] in pent and triangles[i] in hx: 
        print(triangles[i]) 
        break
    i+=1