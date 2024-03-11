vec = [1]

side = 2
for i in range(1001//2):
    vec.append(vec[-1] + side) 
    vec.append(vec[-1] + side)
    vec.append(vec[-1] + side)
    vec.append(vec[-1] + side)
    side+=2
    
print(sum(vec))