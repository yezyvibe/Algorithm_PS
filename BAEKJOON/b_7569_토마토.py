# 최소일수, 퍼져 나간다 -> bfs (O)
import sys
from collections import deque

input = sys.stdin.readline

# 상하좌우위아래
dz = [0, 0, 0, 0, 1, -1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]


def bfs(tomatos):
    q = deque(tomatos)
    max_v = 0
    while q:
        z, x, y = q.popleft()
        for k in range(6):
            nz = z + dz[k]
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if bg[nz][nx][ny] == 0:
                    bg[nz][nx][ny] = bg[z][x][y] + 1
                    q.append((nz, nx, ny))
                    if bg[nz][nx][ny] > max_v:
                        max_v = bg[nz][nx][ny]
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if bg[z][x][y] == 0:
                    return -1
    return max_v - 1


m, n, h = map(int, input().rstrip().split(' '))
bg = [[list(map(int, input().rstrip().split(' '))) for _ in range(n)] for i in range(h)]

tomatos = []
minus_cnt = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if bg[z][x][y] == 1:
                tomatos.append((z, x, y))
            elif bg[z][x][y] == -1:
                minus_cnt += 1
if len(tomatos) + minus_cnt == m * n * h:
    print(0)
else:
    res = bfs(tomatos)
    print(res)
