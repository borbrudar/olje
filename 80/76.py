p = [0]*101
sigma = [0]*101

sigma[1] =1
p[0] = 1

for i in range(2,101):
    for j in range(1,i+1):
        if i%j==0: sigma[i]+=j

for i in range(1,101):
    for k in range(0,i):
        p[i] += sigma[i-k]*p[k]
    p[i]//=i

print(p[100]-1)