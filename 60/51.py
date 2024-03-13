from itertools import permutations

p = [1] * int(1e6+10)
st = set()
p[1]=0
for i in range(2,len(p)):
    if p[i] == 0: continue 
    st.add(i)
    for j in range(i*2,len(p),i): p[j] = 0

n = 6
for choose in range(1,n):
    mask = str("*"*choose)
    for _ in range(n-choose): mask+="_"
    for s in set(permutations(mask)):
        for numbers in range(10**(n-choose),10**(n-choose+1)):
            tmp = str()
            nxt=0
            for i in s:
                if i == "_": 
                    tmp+=str(numbers)[nxt]
                    nxt+=1
                else: tmp+="*"
            
            check = []
            for i in range(0,10):
                if tmp[0]=='0':continue
                t2 = tmp.replace("*",str(i))
                #print(t2)
                if int(t2) in st: 
                    #print(t2)
                    check.append(int(t2))
            if len(check)==8:
                print(check[0])
                exit()