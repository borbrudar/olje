i=1 
while 1:
    if set(str(i)) == set(str(i*2)) and\
    set(str(i)) == set(str(i*3)) and\
    set(str(i)) == set(str(i*4)) and\
    set(str(i)) == set(str(i*5)) and\
    set(str(i)) == set(str(i*6)):
        print(i)
        break    
    i+=1