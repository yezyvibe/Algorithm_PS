t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for l in range(n)]
    cnt = 0
    check = 0

# 가로
    for i in range(n):
        for j in range(n-k+1):
            if arr[i][j] == 1:
                for m in range(k):
                    if arr[i][j+m] == 1:
                        check = 1
                    else:
                        check = 2
                        break
                if check == 1:
                    if j-1 < 0:
                        if arr[i][j + m + 1] == 0:
                            cnt += 1
                    elif j+m+1 >= n:
                        if arr[i][j-1] == 0:
                            cnt += 1
                    else:
                        if arr[i][j-1] == 0 and arr[i][j+m+1] == 0:
                            cnt += 1

# 세로
    for i in range(n-k+1):
        for j in range(n):
            if arr[i][j] == 1:
                for m in range(k):
                    if arr[i+m][j] == 1:
                        check =1
                    else:
                        check = 2
                        break
                if check == 1:
                    if i-1 < 0:
                        if arr[i+m+1][j] == 0:
                            cnt += 1
                    elif i+m+1 >= n:
                        if arr[i-1][j] == 0:
                            cnt += 1  
                    else:
                        if arr[i-1][j] == 0 and arr[i+m+1][j] ==0:
                            cnt += 1
    print('#{} {}'.format(tc, cnt))
