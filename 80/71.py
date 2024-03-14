left = (2,5)
right = (3,7)

while left[1]+right[1]<= int(1e6):
    left = (left[0]+right[0],left[1]+right[1])
    
print(left[0])