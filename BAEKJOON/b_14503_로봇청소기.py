n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
#d: 0북/ 1동/ 2남/ 3서
di = {0:[-1,0], 1:[0,1], 2:[1,0], 3:[0,-1]}


while True:
    arr[r][c] = 2
    tmp_dir = d
    check_flag = False
    for _ in range(4):
        tmp_dir = d-1 if d > 0 else 3
        nr = r + di[tmp_dir][0]
        nc = c + di[tmp_dir][1]
        if arr[nr][nc] == 0:
            d = tmp_dir
            r, c = nr, nc
            check_flag = True
            break
        else:
            d = tmp_dir
    if check_flag:
        continue

    tmp_dir = d - 2 if d > 1 else d + 2
    if arr[r+di[tmp_dir][0]][c+di[tmp_dir][1]] == 1:
        break
    else:
        r += di[tmp_dir][0]
        c += di[tmp_dir][0]

print(sum(arr,[].count(2)))

