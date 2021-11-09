n = int(input())
arr = [[0]*n for k in range(n)]
x = 1
for j in range(n):
    for i in range(n):
        if j % 2 == 0:
            arr[n-1-i][j] = x
            x += 1
        else:
            arr[i][j] = x
            x += 1
for a in arr:
    print(' '.join(map(str, a)))