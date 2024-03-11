from math import factorial

ans=0
for i in range(3,int(1e5)):
    s = 0
    c = i 
    while c>0:
        s+=factorial(c%10)
        c//=10
    if s == i: ans+=i
print(ans)
    