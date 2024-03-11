from math import comb
cnt =0 

for n in range(1,101):
    for r in range(1,n):
        if comb(n,r) > 1_000_000:cnt+=1
        
print(cnt)