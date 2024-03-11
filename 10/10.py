p = [1]*int(2e6)

cnt = 0

for i in range(2,len(p)):
    if p[i]: cnt+=i
    for j in range(i*2,len(p),i): p[j] = 0

print(cnt)