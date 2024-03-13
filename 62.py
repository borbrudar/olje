cubes=dict()
n=int(1e5)
for i in range(1,n):
    cur = list(str(i**3))
    cur.sort()
    cur = str(cur)
    #print(cur)
    if cur in cubes: cubes[cur]+=1
    else : cubes[cur]=1
    
for i in range(1,n):
    if i == 345:
        b=0
    cur = list(str(i**3))
    cur.sort()
    cur = str(cur)
    if cur in cubes and cubes[cur]==5:
        print(i**3)
        break