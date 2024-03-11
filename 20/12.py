import math
i = 0
n = 1
while 1:
    i+= n
    n+=1
    cnt = 0
    for j in range(1,math.isqrt(i)+1):
        if i %j == 0:
            if j*j == i: cnt+=1
            else: cnt+=2
    if cnt > 500: 
        print(i)
        break        
    