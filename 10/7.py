p = [1]*int(2e5)

cnt = 0

for i in range(2,len(p)):
    if p[i]: 
        cnt+=1
    if cnt == 10_001: 
        print(i)
        break
    for j in range(i*2,len(p),i): p[j] = 0