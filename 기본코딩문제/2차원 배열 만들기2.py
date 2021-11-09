n = int(input())
arr = [[0]*n for l in range(n)]
cnt = 1
for j in range(n):
    for i in range(n):
        arr[i][j] = cnt
        cnt += 1
for a in arr:
    print(' '.join(map(str, a)))