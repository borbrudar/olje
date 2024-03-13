with open("59.in") as f:
    vec = list(map(int, f.read().split(",")))

ans=0
alpha = "abcdefghijklmnopqrstuvwxyz"
for a in alpha:
    dec = vec.copy()
    for i in range(0,len(vec),3):
        dec[i] =  chr(vec[i] ^ ord(a))
    for b in alpha:
        for i in range(1,len(vec),3):
            dec[i] = chr(vec[i] ^ ord(b))
        for c in alpha:
            for i in range(2,len(vec),3):
                dec[i] = chr(vec[i] ^ ord(c))
            s = ''.join(dec) 
            if "the" in s and "sums" in s:
                ans=s


print(sum(map(ord,ans)))      
            