ans=1
mx=0
for i in range(1,int(1e6)):
    n = i
    cnt=0
    while n != 1:
        if n%2==0: n//=2
        else : n= 3*n+1
        cnt+=1
    if cnt > mx:
        mx=cnt 
        ans=i
print(ans)