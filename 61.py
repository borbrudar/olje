from itertools import permutations
vec = [set()]
for i in range(6):vec.append(set())
for i in range(1,200): 
    if 1000 <= i*(i+1)//2 < 10000 : vec[0].add(i*(i+1)//2)
for i in range(1,200): 
    if 1000 <= i*i <= 10000 : vec[1].add(i*i)
for i in range(1,200): 
    if 1000 <= i*(3*i-1)//2 < 10000 :vec[2].add(i*(3*i-1)//2)
for i in range(1,200): 
    if 1000 <= i*(2*i-1) < 10000 :vec[3].add(i*(2*i-1))
for i in range(1,200): 
    if 1000 <= i*(5*i-3)//2 < 10000 :vec[4].add(i*(5*i-3)//2)
for i in range(1,200): 
    if 1000 <= i*(3*i-2) < 10000 :vec[5].add(i*(3*i-2))

ans=0
for perm in list(permutations([0,1,2,3,4,5])):
    for a in vec[perm[0]]:
            for c in vec[perm[2]]:
                    for e in vec[perm[4]]:
                            if int(str(a)[2:4] + str(c)[:2]) not in vec[perm[1]]: continue
                            if int(str(c)[2:4] + str(e)[:2]) not in vec[perm[3]]: continue
                            if int(str(e)[2:4] + str(a)[:2]) not in vec[perm[5]]: continue
                            ans= a+c+e+int(str(a)[2:4] + str(c)[:2])+int(str(c)[2:4] + str(e)[:2])+int(str(e)[2:4] + str(a)[:2])
    
print(ans)


# abcd - cdef - efgh - ghij - ijkl - klab
# izberes abcd efgh in ijkl -> 50**3 cca
# 100 moznosti za abcd -> pol se prevers use mozne kombinacije * 720