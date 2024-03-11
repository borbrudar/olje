def isPan(n):
    st = set()
    for i in n:
        if i in st: return False 
        if len(n) < ord(i)-ord('0'): return False
        st.add(i)
    if '0' in st: return False 
    return True 

p = [1] * int(1e7+10)

#print(isPan("2143"))
p[1]=0
ans = 0
for i in range(2,len(p)):
    if p[i] == 0: continue 
    if isPan(str(i)): 
        ans = i
    for j in range(i*2,len(p),i): p[j] = 0
print(ans)