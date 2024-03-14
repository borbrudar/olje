from decimal import *
getcontext().prec = 5000
from math import isqrt
sm=0
for n in range(2,100):
    if isqrt(n)*isqrt(n)==n:continue
    a = Decimal(n).sqrt()
    a = str(a)
    #print(a)
    for i in range(0,101):
        if i == 1: continue
        sm+=int(a[i])
print(sm)