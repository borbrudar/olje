with open("98.in") as f:
    vec = f.read().replace(","," ").replace("\"","").split(" ")
    
l=[]
for i in vec:
    st = set()
    for j in i:
        st.add(j)
    l.append(len(st))
l.sort()
print(l)