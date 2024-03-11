def long(n):
    vec = list()
    i = 0
    start = 1
    while 1:
        while start < n: start*=10
        cur = (start//n,start%n,i) 
        if start%n ==0: return 0
        for j in range(len(vec)):
            if vec[j][0] == cur[0] and vec[j][1] == cur[1]:
                return i-j
        vec.append(cur)  
        i+=1
        start = start%n


mx=0
ans=1
for f in range(2,1000):
    c = long(f)
    #print(c)
    if c > mx: 
        mx = c
        ans=f  
print(ans)