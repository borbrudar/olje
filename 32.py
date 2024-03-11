from itertools import permutations 

st = set()

for a in list(permutations("123456789")):
    s = ''.join(a)
    for i in range(1,7 + 1):
        for j in range(i+1,8 + 1):
            if int(s[0:i]) * int(s[i:j]) == int(s[j:len(s)]): st.add(int(s[j:len(s)]))


print(sum(st))
