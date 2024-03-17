with open("96.in") as f: 
    vec = f.read().split("\n")

n=9

def nxt(y,x):
    x+=1
    if x==n:
        x=0
        y+=1
    return (y,x)

def reduce():
    allowed = []
    for i in range(n):
        allowed.append([])
        for j in range(n):
            allowed[i].append([])
    
    lines = []
    cols = []
    section = []
    for x in range(n):
        cols.append(set())
        for y in range(n):
            if board[y][x] == '0': continue
            cols[-1].add(board[y][x])            
    for y in range(n):
        lines.append(set())
        for x in range(n):
            if board[y][x] == '0': continue
            lines[-1].add(board[y][x])
    for y in range(3):
        section.append([])
        for x in range(3):
            section[y].append([])
            for i in range(3):
                for j in range(3):
                    if board[y*3+i][x*3+j]=='0':continue
                    section[y][x].append(board[y*3+i][x*3+j])
    
    for y in range(n):
        for x in range(n):
            if board[y][x] != '0':
                continue
            for u in range(1,10): 
                ss = str(u)
                if ss not in lines[y] and ss not in cols[x] and ss not in section[y//3][x//3]:
                    allowed[y][x].append(ss)
    return allowed
    
def solve(y,x,allowed):
    if x == 4 and y == 2:
        b=0
    npos = nxt(y,x)
    #print(board)
    if board[y][x] != '0':
        if y == n-1 and x==n-1: return 1
        if solve(npos[0],npos[1],allowed)==1: return 1
        return 0
    
    
    for u in allowed[y][x]:
        board[y][x] = u
        tmp = reduce()
        if y == n-1 and x ==n-1: 
            return 1
        if solve(npos[0],npos[1],tmp) == 1: return 1
    board[y][x] = '0'
    return 0

ans=0
for i in range(len(vec)):
    if vec[i][0] != 'G': continue
    print(i)
    board = []
    for j in range(1,10):
        board.append(list(vec[i+j]))
    tmp =reduce()
    #print(board)
    solve(0,0,tmp)
    #print(board)
    ans += int(str(board[0][0]) + str(board[0][1]) + str(board[0][2]))
print(ans)   