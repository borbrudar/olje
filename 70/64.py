from math import isqrt,gcd
def get_period(n):
    st = set()
    sq = isqrt(n)
    if sq*sq == n: return 0
    #st.add((sq,1,sq)) # rem, top, bot
    rem = sq
    top = 1
    bot = sq # neg actually but joever
        
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
        else : st.add(tmp)
    return 0

print(sum(get_period(i)%2==1 for i in range(1,10001)))