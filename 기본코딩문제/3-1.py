n, m = map(int, input().split())
arr = [[0]*m for k in range(n)]
cnt = 1
for l in range(n+m-1):
    for i in range(m):
        for j in range(n):
            if i+j == l:
                arr[j][i] = cnt
                cnt += 1
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()