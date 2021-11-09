n, m = map(int,input().split())
arr = [[0]*m for k in range(n)]
cnt = 1
for i in range(n+m-1):
    for j in range(n):
        for k in range(m):
            if j+k == i:
                arr[j][k] = cnt
                cnt += 1
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()