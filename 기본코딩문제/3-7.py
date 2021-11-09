n, m = map(int, input().split())
arr = [[0]*m for l in range(n)]
cnt = 1
for k in range(n+m-1):
    for i in range(n):
        for j in range(m):
            if i + j == k:
                arr[n-1-i][j] = cnt
                cnt += 1
for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()