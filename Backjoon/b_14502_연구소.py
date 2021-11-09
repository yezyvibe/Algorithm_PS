import sys
from itertools import combinations as combi
from copy import deepcopy
from collections import deque

# 점점 퍼져 나가는 건 bfs
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
input = sys.stdin.readline


def bfs(virus):
    q = deque()
    for v in virus:
        q.append(v)

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and chk[nx][ny] == 0:
                chk[nx][ny] = 2
                q.append((nx, ny))
    return sum(chk, []).count(0)


n, m = map(int, input().split(' '))
bg = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
virus = []
candidates = []
for i in range(n):
    for j in range(m):
        if bg[i][j] == 2:
            virus.append((i, j))
        elif bg[i][j] == 0:
            candidates.append((i, j))
# print(virus)
# print(candidates)

max_v = -1
for c in combi(candidates, 3):
    chk = deepcopy(bg)
    for x, y in c:
        chk[x][y] = 1
    tmp = bfs(virus)
    if tmp > max_v:
        max_v = tmp

print(max_v)
