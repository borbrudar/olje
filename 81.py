with open("81.in") as f: 
    vec = list(map(lambda line: list(map(int, line.split())), f.read().replace(","," ").split("\n")))
n=80
d = []
vis = []
inf = 1000000000000000
for i in range(len(vec)):
    vis.append([0]*n)
    d.append([inf]*n)



start = (0,0) # y,x
end = (n-1,n-1)

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
    
    if y == n-1 and x == n-1:
        print(d[y][x] + vec[y][x])
        exit()
        
    if y +1 < n and d[y+1][x] > d[y][x] + vec[y][x]: queue.append((-(d[y][x] + vec[y][x]),(y+1,x)))
    if x +1 < n and d[y][x+1] > d[y][x] + vec[y][x]: queue.append((-(d[y][x] + vec[y][x]),(y,x+1)))
    queue.sort(key = lambda a : a[0])
#print(vis)
