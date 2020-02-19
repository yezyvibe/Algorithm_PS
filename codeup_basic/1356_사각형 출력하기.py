n = int(input())
arr = [[' ']*n for l in range(n)]

for i in range(n):
    for j in range(n):
        arr[0][j] = '*'
        arr[n-1][j] = '*'
        arr[i][0] = '*'
        arr[i][n-1] = '*'

for i in range(n):
    for j in range(n):
        print(arr[i][j], end= '')
    print()
