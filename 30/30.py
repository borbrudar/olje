def cnt(n):
    t = n
    s=0
    while t>0:
        s+=(t%10)**5
        t//=10
    return s==n 

ans=0 
for i in range(2,int(2e5)):
    if cnt(i): ans+=i 
print(ans)