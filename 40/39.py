cnt = [0]*1001

for a in range(1,1001):
    for b in range(a,1001):
        for c in range(b,1001):
            if a*a + b*b != c*c : continue 
            if a+b+c>1000:continue 
            cnt[a+b+c]+=1
            
mx=0
val = 0
for i in range(1,1001):
    if cnt[i] > mx:
        mx=cnt[i]
        val=i
print(val)        