vec = [(3,2),(7,5)]
ans=0
for i in range(2,1001):
    vec.append((vec[-1][0]*2 + vec[-2][0],vec[-1][1]*2 + vec[-2][1]))
    if len(str(vec[-1][0])) > len(str(vec[-1][1])):ans+=1
print(ans)