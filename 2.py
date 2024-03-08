vec = [1,2]

cnt = 0
while vec[-1] < 4e6:
    if vec[-1]%2==0: cnt+=vec[-1]
    vec.append(vec[-1] + vec[-2])
print(cnt)