t = 10
for tc in range(1,t+1):
    n = int(input())
    arr = [list(input()) for l in range(8)]
    cnt = 0
#가로 줄
    for a in arr:
        for i in range(8-n+1):
            b = a[i:i + n]
            if b[0:n//2] == b[-1:-(n//2)-1:-1]:
                cnt += 1
#세로 줄
    for i in range(8):
        for j in range(i,8):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    for a in arr:
        for i in range(8-n+1):
            b = a[i:i+n]
            if b[0:n//2] == b[-1:-(n//2)-1:-1]:
                cnt += 1
    print('#{} {}'.format(tc, cnt))