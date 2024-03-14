vec = [2,1,2]
k=2
for i in range(3,50):
   vec.append(1)
   vec.append(1)
   vec.append(2*k) 
   k+=1
   
def rec(i,n):   
   if n==0: return vec[0]
   if i==n: return (1,vec[i])
   cur = vec[i]
   tmp = rec(i+1,n)
   return (tmp[1],cur*tmp[1]+tmp[0])
   
   
s = str(rec(0,99)[1])
sm=0 
for i in s: 
    sm+=ord(i)-ord('0')
print(sm)