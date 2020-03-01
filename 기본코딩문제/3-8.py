n, m = map(int, input().split())
arr = [[0]*m for l in range(n)]
cnt = 1
for k in range(n+m-1):
    for i in range(n):
        for j in range(m):
            if n-1-i + j == k:
                arr[i][j] = cnt
                cnt += 1
for a in arr:
    print(' '.join(map(str, a)))