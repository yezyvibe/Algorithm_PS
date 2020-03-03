dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    n_lst = [0]*(n**2+1)
    max_v = -1

    for i in range(n):
        for j in range(n):
            for k in range(4):
                if 0 <= i+dx[k] < n and 0<= j+dy[k] < n:
                    if arr[i+dx[k]][j+dy[k]] == arr[i][j] + 1:
                        n_lst[arr[i][j]] = 1
                        break

    for i in range(1, n**2):
        if n_lst[i] == 1 and n_lst[i-1] == 0:
            cnt = 1
            while True:
                if n_lst[i+cnt] == 1:
                    cnt += 1
                else:
                    break
            if max_v < (cnt + 1):
                max_v = cnt + 1
                res_num = i
    print('#{} {} {}'.format(t, res_num, max_v))