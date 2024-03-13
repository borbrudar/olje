ans=0
for a in range(1,100):
    for b in range(1,100):
        c = str(a**b)
        s = 0
        for i in c: 
            s+=ord(i)-ord('0')
        ans=max(ans,s)
print(ans)    
            
    