n = int(input())
arr = [[0]*n for l in range(n)]
cnt = 1
for i in range(n):
    for j in range(n):
        if i % 2 == 1:
            arr[i][n-1-j] = cnt
            cnt += 1
        else:
            arr[i][j] = cnt
            cnt += 1

for a in arr:
    print(' '.join(map(str,a)))