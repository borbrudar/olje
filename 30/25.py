f = [1,1]
i = 2


while len(str(f[-1])) < 1000:
    i+=1
    f.append(f[-1]+f[-2])

print(i)
