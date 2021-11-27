import sys

def diffusion(dust):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    tmp_arr = [[0]*c for _ in range(r)]
    while dust:
        x, y = dust.pop()
        before_dust = arr[x][y]
        next_dust = arr[x][y] // 5
        cnt = 0
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                cnt += 1
                tmp_arr[nx][ny] += next_dust
        arr[x][y] = before_dust - (next_dust*cnt)
    for i in range(r):
        for j in range(c):
            if tmp_arr[i][j]:
                arr[i][j] += tmp_arr[i][j]


def move_dust(r, c, air_cleaner):
    r1, c1 = air_cleaner[0]
    r2, c2 = air_cleaner[1]
    # 첫 번째 공기청정기(반시계 방향 회전)
    tmp = 0
    for i in range(1, c):
        tmp, arr[r1][i] = arr[r1][i], tmp
    for i in range(r1-1,-1,-1):
        tmp, arr[i][c-1] = arr[i][c-1], tmp
    for i in range(c-2, -1, -1):
        tmp, arr[0][i] = arr[0][i], tmp
    for i in range(1, r1):
        tmp, arr[i][0] = arr[i][0], tmp

    # 두 번째 공기청정기(시계 방향 회전)
    tmp = 0
    for i in range(1, c):
        tmp, arr[r2][i] = arr[r2][i], tmp
    for i in range(r2+1, r):
        tmp, arr[i][c-1] = arr[i][c-1], tmp
    for i in range(c-2, -1, -1):
        tmp, arr[r-1][i] = arr[r-1][i], tmp
    for i in range(r-2, r2, -1):
        tmp, arr[i][0] = arr[i][0], tmp


input = sys.stdin.readline
r, c, t = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(r)]

for tc in range(t):
    air_cleaner = []
    dust = []
    for i in range(r):
        for j in range(c):
            if arr[i][j]:
                if arr[i][j] == -1:
                    air_cleaner.append((i,j))
                else:
                    dust.append((i, j))
    diffusion(dust)
    move_dust(r, c, air_cleaner)

answer = 0
for a in arr:
    answer += sum(a)
print(answer+2)