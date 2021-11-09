n = int(input())
arr = [[0]*n for k in range(n)]
x = 1
for i in range(len(arr)):
    for j in range(len(arr)):
        arr[i][n-1-j] = x
        x += 1
for a in arr:
    print(' '.join(map(str, a)))