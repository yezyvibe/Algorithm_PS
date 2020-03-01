n, m = map(int,input().split())
arr = [[0]*m for l in range(n)]
cnt = 1
for k in range(n+m-1):
    for j in range(m):
        for i in range(n):
            if i + j == k:
                arr[i][m-j-1] = cnt
                cnt += 1
for a in arr:
    print(' '.join(map(str,a)))