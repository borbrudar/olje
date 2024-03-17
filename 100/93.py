from itertools import permutations


def oppy(l,r,op):
    if op == 0: return l+r
    elif op == 1: return l-r
    elif op == 2: return l*r
    if r == 0: return 10000000000000
    return l/r

def order(l,oper,j):
    if j == 0:
        tmp = oppy(l[0],l[1],oper[0])
        tmp = oppy(tmp,l[2],oper[1])
        return oppy(tmp,l[3],oper[2])
    if j == 1:
        tmp = oppy(l[0],l[1],oper[0])
        tmp2 = oppy(l[2],l[3],oper[2])
        return oppy(tmp,tmp2,oper[1]) 
    if j == 2:
        tmp = oppy(l[1],l[2],oper[1])
        tmp = oppy(l[0],tmp,oper[0])
        return oppy(tmp,l[3],oper[2])
    if j == 3:
        tmp = oppy(l[1],l[2],oper[1])
        tmp = oppy(tmp,l[3],oper[2])
        return oppy(l[0],tmp,oper[0])
    if j == 4:
        tmp = oppy(l[2],l[3],oper[2])
        tmp2 = oppy(l[0],l[1],oper[0])
        return oppy(tmp2,tmp,oper[1])
    if j == 5:
        tmp = oppy(l[2],l[3],oper[2])
        tmp = oppy(l[1],tmp,oper[1])
        return oppy(l[0],tmp,oper[0])
    

mx = 0
epsilon = 1e-9
for a in range(1,10):
    for b in range(a+1,10):
        for c in range(b+1,10):
            for d in range(c+1,10):
                vis = [0]*3025
                digits = [a,b,c,d]
                for perm in list(permutations(digits)):
                    for op1 in range(4):
                        for op2 in range(4):
                            for op3 in range(4):
                                ops = [op1,op2,op3] # 0 -> +, 1-> -, 2-> x, 3 -> /
                                # parenthesis order
                                for o in range(6):
                                    t = order(perm,ops,o)
                                    val = int(round(t))
                                    if abs(t-round(t)) < epsilon and val>=1 and val<=3024: 
                                        vis[val]=1
 

                cr = 0
                for i in range(1,len(vis)):
                    if vis[i]==0:break
                    cr+=1
                if cr > mx:
                    mx=cr
                    ans = str(a)+str(b)+str(c)+str(d)
print(ans)

# (4+2)*3 - 1 = 18-1 = 17 wtf
# 1 + ((3 + 4) * 2) = 7???
# 33 = 1 2 5 8?   

#  1 2 3 4 -> 23 .... 3*4*2 - 1
# note to self: ne dajat b za ime breakpointa ce mas ze variable tak -_-