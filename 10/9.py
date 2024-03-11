for i in range(1,1001):
    for j in range(i+1,1001):
        k = 1000-i-j
        if k <= i or k <= j: continue 
        #print(i,j,k)
        if i*i + j*j == k * k: print(i*j*k)