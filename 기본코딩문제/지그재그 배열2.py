n = int(input())
arr = [[0]*n for l in range(n)]
cnt = 1
for j in range(n):
    for i in range(n):
        if j % 2 == 1:
            arr[n-1-i][j] = cnt
            cnt += 1
        else:
            arr[i][j] = cnt
            cnt += 1
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()