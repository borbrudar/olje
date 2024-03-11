def isPan(n):
    if len(n) != 9: return False 
    st = set()
    for i in n:
        if i in st: return False 
        st.add(i)
    if '0' in st: return False
    return True 

ans =0
i=1 
while 1: 
    s = str(i) + str(i*2)
    if len(s) > 9: break
    j=3
    while len(s) < 9: 
        s += str(i*j)
        j+=1
    if isPan(s): ans=max(ans,int(s))    
    i+=1
print(ans)