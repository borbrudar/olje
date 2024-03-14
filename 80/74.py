from math import factorial

def get_sum(n):
    s=0
    while n>0:
        s+=factorial(n%10)
        n//=10
    return s 


cnt = 0
for i in range(1,int(1e6+1)):
    s=set()
    cur=i
    while cur not in s: 
        s.add(cur)
        cur=get_sum(cur)
    if len(s) == 60:cnt+=1

print(cnt)