from random import randrange
import random
squares = [0]*40

cc = [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ch = [1,2,3,4,5,6,7,7,8,9,0,0,0,0,0,0]
random.shuffle(cc)
random.shuffle(ch)


ccp = 0
chp = 0
steps = int(1e6)

cur = 0
jail = 10
g2j = 30
doubles=0
for i in range(steps):
    if cur == jail:
        doubles=0
    k1 = randrange(0,5)
    k2 = randrange(0,5)
    k = k1+k2
    cur += k
    cur%=40
    if k1 == k2: doubles +=1
    else: doubles=0
    if doubles == 3:
        cur=jail
        continue
    if cur == g2j: cur = jail

    # cc
    if cur == 2 or cur == 17 or cur == 33:
        if cc[ccp] == 1:cur = 0
        elif cc[ccp] == 2: cur = jail     
        ccp+=1
        ccp%=16

    # ch
    if cur == 7 or cur == 22 or cur == 36:
        if ch[chp] == 1: cur = 0
        elif ch[chp] == 2: cur = jail
        elif ch[chp] == 3: cur = 11 # c1
        elif ch[chp] == 4: cur = 24 # e3
        elif ch[chp] == 5: cur = 39 # h2
        elif ch[chp] == 6: cur = 5 # r1
        elif ch[chp] == 7:
            if cur == 7: cur = 15 # r2
            elif cur == 22: cur = 25 #r3
            elif cur == 36: cur =5 #r4
        elif ch[chp] == 8:
            if cur == 7: cur = 12 # u1
            elif cur == 22: cur = 28 #u2
            elif cur == 36: cur = 12 #u1
        elif ch[chp] == 9: 
            cur = cur-3+40
            cur%=40
        
        chp+=1
        chp%=16

    squares[cur]+=1

mx = [0,0,0]
vals = [0,0,0]
for i in range(len(squares)):
    cur = squares[i]/steps
    if cur > mx[0]:
        mx[2] = mx[1]
        vals[2] = vals[1]
        mx[1] = mx[0]
        vals[1] = vals[0]
        mx[0] = cur
        vals[0] = i
    elif cur > mx[1]:
        mx[2] = mx[1]
        vals[2]=vals[1]
        mx[1] = cur
        vals[1]= i 
    elif cur > mx[2]:
        mx[2] = cur
        vals[2] = i
ans = str()
for i in range(3):
    if vals[i] < 10: ans+=" "+str(vals[i])
    else: ans+=str(vals[i])
print(ans)