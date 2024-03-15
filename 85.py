
# nm = (n+1)*n/2 + (m+1)*m/2
n=1000
m=1000
ans = 0
diff = 200000000000

for n in range(1,2000):
    for m in range(1,2000):
        cur = (n+1)*n//2 * (m+1)*m//2
        if abs(cur-2_000_000) < diff:
            diff = abs(cur-int(2e6))
            ans = n*m 
print(ans)