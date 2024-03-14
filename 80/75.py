from math import isqrt
L = 1_500_001
div = []*L
for i in range(L): div.append([1,i])

for i in range(2,len(div)):
    for j in range(i*2,len(div),i):div[j].append(i)

ans=0
for i in range(2,L):
    #if i%10000==0:  print(i)
    cnt=0
    st=set()
    for a in div[i]:
        for b in div[i]: 
            if a*b%2==0: st.add(a*b//2)
    for asd in st:
        x=asd
        y = i*i//(2*x)
        # x = i-a, a = i-x
        if x >= i or x <= 0: continue 
        if y >= i or y <= 0: continue 
        cnt+=1         
        if x == y: cnt+=1
    cnt//=2    
    if cnt==1:ans+=1
print(ans)    

# i**2 = 2(i-a)(i-b)
# ok we can find all divisors of i**2/2 by finding 
# all divisors of i
# 60 - (34) = 26
# 12**2 == 2*(12-3)(12-4)