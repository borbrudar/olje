vec = [1,2,5,10,20,50,100,200]

dp = [0]*201
dp[0]=1

last = 0

for u in vec:
    for i in range(1,201):
        if u <= i: dp[i] += dp[i-u]
                   
#print(dp)
print(dp[-1])