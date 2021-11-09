n = int(input())
arr = [[0]*n for l in range(n)]
cnt = 1
for i in range(n,0,-1):
    for j in range(n,0,1):
        arr[0][j//2] = 1
        cnt += 1
        arr[i][j] = cnt
        if i < 0:
            i =

