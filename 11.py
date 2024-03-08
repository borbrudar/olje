with open("11.in") as f: 
    arr = list(map(lambda line: list(map(int, line.split())), f.read().split("\n")))

ans = 0

for i in range(20):
    for j in range(20):
        if i <= 16: 
            ans = max(ans,arr[i][j]*arr[i+1][j]*arr[i+2][j] * arr[i+3][j])
        if j <= 16: 
            ans = max(ans,arr[i][j]*arr[i][j+1]*arr[i][j+2] * arr[i][j+3])
        if i <= 16 and j <= 16: 
            ans = max(ans,arr[i][j]*arr[i+1][j+1]*arr[i+2][j+2] * arr[i+3][j+3])
        if i <= 16 and j >= 3: 
            ans = max(ans,arr[i][j]*arr[i+1][j-1]*arr[i+2][j-2] * arr[i+3][j-3])
            
print(ans)