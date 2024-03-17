cnt=0
n = 51
for x1 in range(n):
    for y1 in range(n):
        a = x1**2 + y1**2
        if x1 == 0 and y1==0: continue
        for x2 in range(n):
            for y2 in range(n):
                if x2==0 and y2==0 :continue
                if x1==x2 and y1==y2:continue
                b = x2**2 + y2**2
                c = (x1-x2)**2 + (y1-y2)**2
                if a+b==c or a+c==b or b+c==a:
                    cnt+=1
cnt//=2
print(cnt)