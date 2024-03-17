# heron prav p = sqrt(s(s-a)(s-b)(s-c))
# torej s(s-a)(s-b)(s-c) = x^2
# dva stranici sta isti torej
# s(s-a)(s-c)^2 = x^2
# s(s-a) = y^2
# (a+b+c)/2  * ((b+c-2a)/2) = 1/2 * ( a+2c)(c-a) = y^2
# raj nebi korenu sm zgleda da ni druge
from math import isqrt
n = int(1e9)//3
cnt=0
for a in range(2,n):
    c = a+1
    up = (2*a+c)*c*c*(2*a-c)
    if up%16!=0:continue
    up//=16
    s=isqrt(up)
    if s*s==up:
        cnt+=2*a+c

for a in range(2,n):
    c = a-1
    up = (2*a+c)*c*c*(2*a-c)
    if up%16!=0:continue
    up//=16
    s=isqrt(up)
    if s*s==up:
        cnt+=2*a+c  
        
print(cnt) 