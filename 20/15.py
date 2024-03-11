n=21
arr = [[0]*n for _ in range(n)]
arr[0][0] = 1

for i in range(n):
    for j in range(n):
        if i > 0: arr[i][j] += arr[i-1][j]
        if j > 0: arr[i][j] += arr[i][j-1]

print(arr[n-1][n-1])