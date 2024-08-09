with open("89.in") as f:
     vec = f.read().split("\n")


def get_val(s):
    cur =0 
    i = 0
    while i < len(s):
        if s[i] == 'M':
            cur+=1000
            i+=1
            continue
        if s[i] == 'D':
            cur+=500
            i+=1
            continue
        if s[i] == 'L':
            cur+=50
            i+=1
            continue
        if s[i] == 'V':
            cur+=5
            i+=1
            continue
        if s[i] == 'C':
            if i+1==len(s):
                cur+=100
                break
            if s[i+1] == 'D':
                cur += 400
                i+=2
                continue
            if s[i+1] == 'M':
                cur += 900
                i+=2
                continue
            cur+=100
            i+=1
            continue
        if s[i] == 'X':
            if i+1==len(s):
                cur+=10
                break
            if s[i+1] == 'L':
                cur += 40
                i+=2
                continue
            if s[i+1] == 'C':
                cur += 90
                i+=2
                continue
            cur+=10
            i+=1
            continue
        if s[i] == 'I':
            if i+1==len(s):
                cur+=1
                break
            if s[i+1] == 'V':
                cur += 4
                i+=2
                continue
            if s[i+1] == 'X':
                cur += 9
                i+=2
                continue
            cur+=1
            i+=1
            continue
    return cur


def best(n):
    cur = 0
    s = str()
    while n > 0:
        if n >= 1000: 
            n-=1000
            cur+=1
            s += "M"
            continue
        if n >= 900:
            n-=900
            cur+=2
            s += "CM"
            continue
        if n>=500:
            n-=500
            cur+=1
            s+="D"
            continue
        if n>=400: 
            n-=400
            cur+=2
            s+="CD"
            continue
        if n>=100:
            n-=100
            cur+=1
            s+="C"
            continue
        if n>=90:
            n-=90
            cur+=2
            s+="XC"
            continue
        if n>=50:
            n-=50
            cur+=1
            s+="L"
            continue
        if n>=40:
            n-=40
            cur+=2
            s+="XL"
            continue
        if n>=10:
            n-=10
            cur+=1
            s+="X"
            continue
        if n>=9:
            n-=9
            cur+=2
            s+="IX"
            continue
        if n>=5:
            n-=5
            cur+=1
            s+="V"
        if n>=4:
            n-=4
            cur+=2
            s+="IV"
            continue
        if n>=1:
            n-=1
            s+="I"
            cur+=1    
    return cur

ans =0
for i in vec:
    #b = best(get_val(i))
    #print(i,b)
    ans+=len(i) - best(get_val(i))
print(ans)