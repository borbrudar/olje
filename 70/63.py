cnt=0

for i in range(1,10):
    n = 1
    while len(str(i**n)) == n: 
        cnt+=1
        n+=1

print(cnt)