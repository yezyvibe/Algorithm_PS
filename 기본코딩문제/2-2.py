n = int(input())
arr = [[0]*n for k in range(n)]
x = 1
for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            arr[i][n-1-j] = x
            x += 1
        else:
            arr[i][j] = x
            x += 1
for a in arr:
    print(' '.join(map(str, a)))