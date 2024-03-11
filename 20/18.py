with open("18.in") as f: 
    arr = list(map(lambda line: list(map(int, line.split())), f.read().split("\n")))

for i in range(1,len(arr)):
    for j in range(1,len(arr[i])):
        if j == len(arr[i])-1: arr[i][j] += arr[i-1][j-1]
        elif j == 0: arr[i][j] += arr[i-1][j]
        else: arr[i][j] += max(arr[i-1][j], arr[i-1][j-1])
        
print(max(arr[-1]))