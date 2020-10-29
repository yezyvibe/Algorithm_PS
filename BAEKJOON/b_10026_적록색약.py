import sys
from copy import deepcopy

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(start, color):
    s = [start]
    while s:
        x, y = s.pop()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and chk[nx][ny] != 1:
                if bg[nx][ny] == color:
                    chk[nx][ny] = 1
                    s.append((nx, ny))


def rg_dfs(start, color):
    s = [start]
    if color == 'B':
        c = ['B']
    else:
        c = ['R', 'G']
    while s:
        x, y = s.pop()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and chk[nx][ny] != 1:
                if bg[nx][ny] in c:
                    chk[nx][ny] = 1
                    s.append((nx, ny))


n = int(input())
bg = [list(input().rstrip()) for _ in range(n)]
chk = deepcopy(bg)
rg_cnt = 0
for i in range(n):
    for j in range(n):
        if chk[i][j] != 1:
            color = bg[i][j]
            rg_dfs((i, j), color)
            rg_cnt += 1


chk = deepcopy(bg)
cnt = 0
for i in range(n):
    for j in range(n):
        if chk[i][j] != 1:
            color = bg[i][j]
            dfs((i, j), color)
            cnt += 1

print(cnt, rg_cnt)