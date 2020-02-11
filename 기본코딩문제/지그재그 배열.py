n =int(input())
arr = [[0]*n for l in range(n)]
cnt = 1
for k in range(n-1,2*n-1):
    for j in range(n):
        for i in range(n):
            if n % 2 == 0:
                if i + j == k:
                    if k % 2 == 1:
                        arr[i][j] = cnt
                        cnt += 1
                    else:
                        arr[j][i] = cnt
                        cnt += 1
            else:
                if i + j == k:
                    if k % 2 == 0:
                        arr[i][j] = cnt
                        cnt += 1
                    else:
                        arr[j][i] = cnt
                        cnt += 1
for a in arr:
    print(' '.join(map(str,a)))