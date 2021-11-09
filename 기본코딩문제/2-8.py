n, m = list(map(int,input().split()))
arr = [[0]*m for k in range(n)]
x = 1
for j in range(m):
    for i in range(n):
        if j % 2 == 0:
            arr[i][m-1-j] = x
            x += 1
        else:
            arr[n-1-i][m-1-j] = x
            x += 1
for a in arr:
    print(' '.join(map(str, a)))