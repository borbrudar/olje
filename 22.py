with open("22.in") as f:
    vec = f.read().replace("\"","").split(",")

vec.sort()
cnt=0
for i in range(len(vec)):
    score= 0
    for j in vec[i]:
        score+=ord(j)-ord('A')+1
    cnt += (i+1)*score
print(cnt)