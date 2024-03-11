def isPal(s):
    s=str(s)
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]: return False    
    return True

ans=0
for i in range(1,10002):
    ok = 1
    cur=i
    for _ in range(52):
        c = (str(cur)[::-1])
        while c[0] == "0": c=c[1:]
        cur += int(c)
        if isPal(cur): 
            ok=0
            break               
    if ok: ans+=1
    
print(ans)