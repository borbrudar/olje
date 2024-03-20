# 0000000000 -> 10 bitov za prvo, 10 za drugo
def main():
    sq = ["01","04","09","16","25","36","49","64","81"]

    i = -1
    cnt=0
    while i < (1<<20):
        i+=1
        cur = i
        six = 0
        for j in range(0,10):
            if (cur>>j)&1==1:six+=1
        if six!=6:continue
        six=0
        for j in range(10,20):
            if (cur>>j)&1==1: six+=1
        if six!=6: continue

        if (cur>>6)&1 == 1:
            cur |= (1<<9)
        if (cur>>16)&1 == 1:
            cur |= (1<<19)
        if (cur>>9)&1 == 1:
            cur |= (1<<6)
        if (cur>>19)&1 == 1:
            cur |= (1<<16)

        ok =1
        for s in sq:
            cc=0
            f = ord(s[0])-ord('0')
            s = ord(s[1])-ord('0')
            if (cur>>f)&1==1 and (cur>>(s+10))&1==1:cc=1
            elif (cur>>s)&1==1 and (cur>>(f+10))&1==1: cc=1        
            ok&=cc
        if ok==1:cnt+=1
    print(cnt//2)
    
main()