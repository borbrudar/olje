d = {
    "2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
    "T":10,"J":11,"Q":12,"K":13,"A":14
}

def has22(h):
    # * * * * _
    if h[0][0] == h[1][0] and h[2][0] == h[3][0]: return (1,d[h[3][0]])
    # * * _ * *
    if h[0][0] == h[1][0] and h[3][0] == h[4][0]: return (1,d[h[3][0]])
    # _ * * * *
    if h[1][0] == h[2][0] and h[3][0] == h[4][0]: return (1,d[h[3][0]])
    return (0,0)

def has2(h):
    if h[4][0] == h[3][0]: return (1,d[h[4][0]])
    if h[3][0] == h[2][0]: return (1,d[h[3][0]])
    if h[2][0] == h[1][0]: return (1,d[h[2][0]])
    if h[1][0] == h[0][0]: return (1,d[h[1][0]])
    return (0,0)

def has3(h):
    if h[0][0] == h[2][0]: return (1,d[h[2][0]])
    if h[1][0] == h[3][0]: return (1,d[h[3][0]])
    if h[2][0] == h[4][0]: return (1,d[h[4][0]])
    return (0,0)
    

def rank(h):
    h.sort(key=lambda x : d[x[0]])
    same_suit = h[0][1] == h[1][1] and h[1][1] == h[2][1] and\
        h[2][1] == h[3][1] and h[3][1] == h[4][1]
    consecutive = d[h[0][0]]+1 == d[h[1][0]] and d[h[1][0]]+1==d[h[2][0]] and\
        d[h[2][0]]+1== d[h[3][0]] and d[h[3][0]]+1==d[h[4][0]]
    last = d[h[4][0]]
    #royal flush, no ties here
    if h[0][0] == "T" and h[1][0] == "J" and h[2][0] == "Q" and h[3][0] == "K"\
    and h[4][0] == "A" and same_suit:
            return (10,0)
    # straight flush >_<
    if  consecutive and same_suit: return (9, last)
    #four 
    if h[0][0] == h[3][0]: return (8,d[h[0][0]])
    if h[1][0] == h[4][0]: return (8,d[h[1][0]])
    # full house
    if h[0][0] == h[2][0] and h[3][0] == h[4][0]:
        return (7,d[h[2][0]])
    if h[0][0] == h[1][0] and h[2][0]==h[4][0]:
        return (7, d[h[4][0]])
    #flush
    if same_suit: return (6,last)
    # straight >_<
    if consecutive: return (5,last)
    # three
    three = has3(h)
    if three[0] == 1: return (4,three[1])
    # pairs
    tt = has22(h)
    if tt[0]==1: return (3,tt[1])
    # pair
    two = has2(h)
    if two[0]==1: return (2, two[1])
    #high
    return (1,last)

def cmp_by_size(p1,p2):
    p1.sort(key=lambda x : d[x[0]])
    p2.sort(key=lambda x : d[x[0]])
    for i in range(4,-1,-1):
        if d[p1[i][0]] > d[p2[i][0]]: return 1
        elif d[p2[i][0]] > d[p1[i][0]]: return 0
    return 0

with open("54.in") as f:
    vec = f.read().replace("\n"," ").split(" ")
    

cnt = 0
while len(vec)>0:
    p2 = []
    for _ in range(5):
        p2.append(vec[-1])
        vec.pop()
    p1 = []
    for _ in range(5):
        p1.append(vec[-1]) 
        vec.pop()
    r1=rank(p1)
    r2=rank(p2)
    if r1[0] > r2[0] or (r1[0]==r2[0] and r1[1]>r2[1]): 
        cnt+=1
        continue 
    if r2[0] > r1[0] or (r1[0]==r2[0] and r1[1]<r2[1]): continue 
    if cmp_by_size(p1,p2)==1: cnt+=1
    
print(cnt)