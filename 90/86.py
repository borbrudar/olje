
def main():
    st = set()
    for i in range(int(1e7)):
        st.add(i*i)


    cnt =0
    for a in range(1,2500):
            if a%10==0:print(a)
            for b in range(1,a+1):
                for c in range(b,a+1):
                    mn = a*a+(b+c)**2
                    vv = (a+c)**2 + b**2
                    if vv < mn:
                        mn = vv
                    vv = (a+b)**2+c**2
                    if vv < mn: mn=vv
                    if mn in st: cnt+=1
            if cnt > 1_000_000: 
                print(a)
                break
    
main()