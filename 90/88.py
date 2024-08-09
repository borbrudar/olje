# torej zgleda da je navzgor omejeno s k*2, torej lahko preverjamo samo vsote do nekje 24k
# pc ce je k sod, potem lhk zmeri das k/2 * 2 * 1..... = k/2 + 2  + 1... etc.
# zgornja meja je torej 2k, spodnja je ocitno k (1+1....)...mamo kasno monotonost kle slucajnu? hm dvomm
# lhk bi za vsako stevilo najdl use mozne nacine da ga razceps u product-sum sm fak kk bi tu naredu
# ig bi su cez delitelje pa preveru ce je ok usota???

import sys,functools
from math import isqrt
#sys.setrecursionlimit(100000)

@functools.lru_cache(maxsize=25000000)
def check(val,div,s, number_of_elements): # s je sum, div so se unallocated values 
    if s > val or div == 1: return
    nm = number_of_elements + val-s # paddamo z enkami
    if nm <= 12000 and vec[nm] == 0: vec[nm] = val
    for i in range(2,isqrt(div)+1):
        if div%i != 0: continue
        check(val, div//i, s - div + i + div//i, number_of_elements + 1)
        other = div//i
        check(val, div//other, s - div + other + div//other, number_of_elements+1)

vec = [0]*12001 # rezultat

for i in range(2,24010):
    check(i, i, i, 1)
    
summed = set()
ans=0
for i in range(2,12001):
    if vec[i] not in summed:
        ans += vec[i]
        summed.add(vec[i])       
#print(vec[:13])
print(ans)