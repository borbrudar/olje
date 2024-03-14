from math import isqrt
vec=[]
def get_period(n):
    vec.clear()
    st = set()
    sq = isqrt(n)
    if sq*sq == n: return 0
    #st.add((sq,1,sq)) # rem, top, bot
    rem = sq
    top = 1
    bot = sq # neg actually but joever
    vec.append(sq)
    while 1:
        ntop = bot
        nbot = (n-bot*bot)//top
        rem = 0
        while ntop - nbot >= -sq: 
            rem+=1
            ntop-=nbot
        ntop=-ntop

        top = nbot
        bot = -(bot - rem*nbot) 
        tmp = (rem,top,bot)
        if tmp in st: return len(st)
        else : 
            st.add(tmp)
            vec.append(rem)
    return 0


def rec(i,n):   
   if n==0: return vec[0]
   if i==n: return (1,vec[i])
   cur = vec[i]
   tmp = rec(i+1,n)
   return (tmp[1],cur*tmp[1]+tmp[0])


def get_min(n):
    p = get_period(n)
    if p%2==0: tmp=rec(0,p-1)
    else : 
        for i in range(len(vec)): vec.append(vec[i])
        tmp=rec(0,2*p-1)
    return tmp[1]

mx=0
ans=0
for i in range(1,1001):
    if isqrt(i)*isqrt(i) == i: continue
    d=get_min(i)
    if d > mx:
        mx=d
        ans=i
print(ans)