import sys
sys.setrecursionlimit(1000000)
cnt = 3

def calc(left,right):
    a = left[0]
    b= left[1] 
    c=right[0]
    d=right[1]
    if b+d > 12000: return 0
    return 1 + calc(left, (a+c,b+d)) + calc((a+c,b+d),right)


cnt+=calc((1,3),(3,8))
cnt+=calc((3,8),(2,5))
cnt+=calc((2,5),(3,7))
cnt+=calc((3,7),(1,2))

print(cnt)