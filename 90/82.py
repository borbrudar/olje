with open("81.in") as f: 
    vec = list(map(lambda line: list(map(int, line.split())), f.read().replace(","," ").split("\n")))
n=80

def dijsktra(start,end):
    d = []
    vis = []
    inf = 1000000000000000
    for i in range(len(vec)):
        vis.append([0]*n)
        d.append([inf]*n)

    #start = (0,0) # y,x
    #end = (n-1,n-1)

    queue = [] # -dist, node ???
    queue.append((0,start))

    while len(queue) > 0:
        cur = queue[-1]
        queue.pop()
        dist = -cur[0]
        y = cur[1][0]
        x = cur[1][1]
        if vis[y][x] == 1: continue
        vis[y][x]=1
        d[y][x] = dist

        if y == end[0] and x == end[1]:
            return d[y][x] + vec[y][x]

        if y +1 < n and d[y+1][x] > d[y][x] + vec[y][x]: queue.append((-(d[y][x] + vec[y][x]),(y+1,x)))
        if x +1 < n and d[y][x+1] > d[y][x] + vec[y][x]: queue.append((-(d[y][x] + vec[y][x]),(y,x+1)))
        if y -1 >= 0 and d[y-1][x] > d[y][x] + vec[y][x]: queue.append((-(d[y][x] + vec[y][x]),(y-1,x)))
        queue.sort(key = lambda a : a[0])
    #print(vis)

ans= 1000000000000000000
for left in range(n):
    print(left)
    for right in range(n):
        ans=min(ans,dijsktra((left,0),(right,n-1)))
print(ans)  