from math import gcd
ans = (1,1)

for num in range(10,100):
    for den in range(10,100):
        if num%10 == 0 and den%10 ==0: continue
        simp = -1
        if num == 49 and den == 98:
            b =0
        if str(num)[0] == str(den)[0]:
            simp = (int(str(num)[1]), int(str(den)[1]))
            if not (simp == (num//gcd(num,den),den//gcd(num,den)) and simp[0] < simp[1]): simp=-1 
        elif str(num)[0] == str(den)[1]:
            simp = (int(str(num)[1]),  int(str(den)[0]))
            if not (simp == (num//gcd(num,den),den//gcd(num,den)) and simp[0] < simp[1]): simp=-1
        elif str(num)[1] == str(den)[0]:
            simp = (int(str(num)[0]) , int(str(den)[1]))
            g = gcd(simp[0],simp[1])
            simp = (simp[0]//g,simp[1]//g)
            if not (simp == (num//gcd(num,den),den//gcd(num,den)) and simp[0] < simp[1]): simp=-1
        elif str(num)[1] == str(den)[1]: 
            simp = (int(str(num)[0]), int(str(den)[0]))
            if not (simp == (num//gcd(num,den),den//gcd(num,den)) and simp[0] < simp[1]): simp=-1
        if simp == -1: continue
        #print(num,den)
        ans = (ans[0] * simp[0],ans[1] * simp[1])
        
        
print(ans[1]//gcd(ans[1],ans[0]))