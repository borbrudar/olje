vec = list(set())

p = [1] * int(1e6+10)
p[1]=0
for i in range(2,len(p)+10):vec.append(set() )

for i in range(2,len(p)):
    if p[i] == 0: 
        continue
    for j in range(i*2,len(p),i): 
        p[j]=0
        vec[j].add(i)
        
#print(vec[644])
#print(vec[645])
#print(vec[646])
#print(vec[644]-vec[645])

for i in range(3,len(vec)-4):
    if vec[i]-vec[i+1]==vec[i] and vec[i+1]-vec[i+2]==vec[i+1] \
        and vec[i+2]-vec[i+3]==vec[i+2] and len(vec[i])==4 and\
            len(vec[i+1])==4 and len(vec[i+2])==4 and len(vec[i+3])==4:
            print(i)
            break        