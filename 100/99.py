with open("99.in") as f: 
    vec = list(map(lambda line: list(map(int, line.split())), f.read().replace(","," ").split("\n")))


for i in range(len(vec)):
    u=vec[i]
    ok = 1
    
    for cmp in vec:
        if u == cmp: continue
        if pow(u[0],u[1]/cmp[1]) < cmp[0]:
            ok=0
            break    
    if ok == 1:
        print(i+1)
        break