triangles = set()

for i in range(1,int(1e6)):
    triangles.add(i*(i+1)//2)
    
with open("42.in") as f:
    vec = f.read().replace("\"","").split(",")

cnt = 0
for s in vec:
    cur=0
    for j in s:
        cur+=ord(j)-ord('A')+1
    if cur in triangles: cnt+=1
print(cnt) 