def isPal(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]: return False    
    return True

ans=0
for i in range(1,int(1e6+1)):
    s = str()
    n = i 
    while n>0: 
        if n%2==0: s+="1"
        else: s+="0"
        n//=2
    s=s[::-1]      
    if isPal(str(i)) and isPal(s): ans+=i

print(ans)