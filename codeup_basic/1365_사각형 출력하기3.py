n = int(input())
arr = [[' ']*n for l in range(n)]

for i in range(n):
    for j in range(n):
        arr[0][j] = '*'
        arr[i][0] = '*'
        arr[i][n-1] = '*'
        arr[n-1][j] = '*'
        if i == j:
            arr[i][j] = '*'
        if i + j == n-1:
            arr[i][j] = '*'

for a in arr:
    print(''.join(map(str, a)))