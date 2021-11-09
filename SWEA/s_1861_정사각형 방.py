# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for t in range(1,int(input())+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    res_cnt = -1
    res_start = 0
    for i in range(n):
        for j in range(n):
            tx = i
            ty = j
            start = arr[i][j]
            cnt = 1
            while True:
                for k in range(4):
                    ni = tx+dx[k]
                    nj = ty+dy[k]
                    if (0<= ni <n and 0<= nj <n and arr[ni][nj] - arr[tx][ty] == 1):
                        tx = ni
                        ty = nj
                        cnt += 1
                        break
                else:
                    break

            if cnt > res_cnt:
                res_cnt = cnt
                res_start = start
            elif cnt == res_cnt:
                if res_start > start:
                    res_start = start
    print('#{} {} {}'.format(t, res_start, res_cnt))